# method_of_joints.py

import numpy as np

def calculate_joint_forces(nodes, beams):
    joint_forces = {}

    for i, node in enumerate(nodes):
        Fx, Fy = node[2], node[3]
        joint_forces[i] = {"Fx": Fx, "Fy": Fy, "beams": []}

    for i, beam in enumerate(beams):
        node1, node2 = beam[0], beam[1]
        joint_forces[node1]["beams"].append(i)
        joint_forces[node2]["beams"].append(i)

    A = []
    b = []

    for i, node in enumerate(nodes):
        if joint_forces[i]["Fx"] != 0 or joint_forces[i]["Fy"] != 0:
            A_row1 = [0] * len(beams)
            A_row2 = [0] * len(beams)
            for beam_index in joint_forces[i]["beams"]:
                beam = beams[beam_index]
                node1, node2 = beam[0], beam[1]
                x1, y1 = nodes[node1][0], nodes[node1][1]
                x2, y2 = nodes[node2][0], nodes[node2][1]
                length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if i == node1:
                    A_row1[beam_index] = (x2 - x1) / length
                    A_row2[beam_index] = (y2 - y1) / length
                else:
                    A_row1[beam_index] = (x1 - x2) / length
                    A_row2[beam_index] = (y1 - y2) / length
            A.append(A_row1)
            A.append(A_row2)
            b.append(-joint_forces[i]["Fx"])
            b.append(-joint_forces[i]["Fy"])

    A = np.array(A)
    b = np.array(b)

    beam_forces = np.linalg.solve(A, b)

    return beam_forces
