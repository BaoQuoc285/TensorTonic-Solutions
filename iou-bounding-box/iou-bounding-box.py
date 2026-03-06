def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    
    A = max(box_a[0],box_b[0])
    B = max(box_a[1],box_b[1])
    C = min(box_a[2],box_b[2])
    D = min(box_a[3],box_b[3])
    if C <= A or D <= B:
        return 0
    overlap = (C-A)*(D-B)
    union = (box_a[2] -box_a[0])*(box_a[3]-box_a[1]) + (box_b[2] -box_b[0])*(box_b[3]-box_b[1]) - overlap
    
    return overlap/union