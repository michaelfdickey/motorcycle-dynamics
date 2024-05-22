# method_of_joints.py

import numpy as np

def calculate_joint_forces(nodes, beams, fixtures, masses):
    num_nodes = len(nodes)
    num_beams = len(beams)
    
    A = np.zeros((2 * num_nodes, num_beams))
    b = np.zeros(2 * num_nodes)
    
    # Populate the A matrix and b vector
    for i, (node1_idx, node2_idx) in enumerate(beams):
        x1, y1 = nodes[node1_idx]
        x2, y2 = nodes[node2_idx]
        length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        cos_theta = (x2 - x1) / length
        sin_theta = (y2 - y1) / length
        
        # Node1 equations
        A[2 * node1_idx, i] = cos_theta
        A[2 * node1_idx + 1, i] = sin_theta
        # Node2 equations
        A[2 * node2_idx, i] = -cos_theta
        A[2 * node2_idx + 1, i] = -sin_theta
    
    # Apply forces (assuming forces and masses are provided for all nodes)
    for i, (fx, fy) in enumerate(masses):
        b[2 * i] = fx
        b[2 * i + 1] = fy

    # Solve the system
    try:
        beam_forces = np.linalg.lstsq(A, b, rcond=None)[0]
    except np.linalg.LinAlgError:
        print("Incompatible dimensions in A and b")
        return None

    return beam_forces

def differentiate_forces(beam_forces):
    """
    Differentiate between tension and compression forces.
    Positive values indicate tension, negative values indicate compression.
    """
    tension_compression = {}
    for i, force in enumerate(beam_forces):
        if force > 0:
            tension_compression[i] = "Tension"
        else:
            tension_compression[i] = "Compression"
    return tension_compression