"""
Takes input text file of coco formatted data, and outputs tables.
"""

import sys

assert len(sys.argv) == 2, "ONE file path should be specified."

coco = sys.argv[1]

with open(coco, 'r') as f:
    prev = "(AR)"
    for l in f:
        l_s = l.split()
        if l_s:
            if l_s[0] == "Evaluating":
                print(l, end="")

            elif l_s[0] == "Average":
                #print(l, end="")
                # print if precision or recall
                if prev != l_s[2]:
                    print(l_s[2])
                    prev = l_s[2]

                # IoU
                iou = l_s[4].split("=")[1]
                iou = iou.split(":")
                if len(iou) == 1:
                    iou.append("")

                print("$[" + iou[0] + ", " + iou[1] + "]$" , " & ", end="")
                l_s2 = l.split("|")
                # Area
                print(l_s2[1].split("=")[1], " & ", end="")
                # maxDets
                print(l_s2[2].split()[0].split("=")[1], " & ", end="")
                # score
                print(l_s[-1], "\\\\")
