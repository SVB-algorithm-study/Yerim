class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = []
        pdict = set(positive_feedback)
        ndict = set(negative_feedback)
        for idx, rep in enumerate(report):
            slst = rep.split()
            point = 0
            for s in slst:
                if s in pdict:
                    point += 3
                elif s in ndict:
                    point -= 1
            l.append([-point, student_id[idx]])
        l.sort()
        ans = []
        for e in l[:k]:
            ans.append(e[1])
        return ans