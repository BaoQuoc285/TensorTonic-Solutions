def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    # Write code here
    def IoU_score(box1, box2):
        if len(box1) != len(box2):
            raise NameError('Do Not same Shape')
        A = max(box1[0],box2[0])
        B = max(box1[1],box2[1])
        C = min(box1[2],box2[2])
        D = min(box1[3],box2[3])
        overlap = (C-A)*(D-B)
        union = (box1[2]-box1[0])*(box1[3]-box1[1]) + (box2[2]-box2[0])*(box2[3]-box2[1]) - overlap
        return overlap/union

    box_score = list(zip(boxes,scores))
    order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    keep = []
    while order:
        i = order.pop(0)
        keep.append(i)
        order = [ j for j in order if IoU_score(boxes[i],boxes[j]) < iou_threshold ]
    return keep
            
        
    
    
    