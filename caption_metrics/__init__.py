__author__ = 'tylin'
from .tokenizer.ptbtokenizer import PTBTokenizer
from .bleu.bleu import BLEU
from .meteor.meteor import METEOR
from .rouge.rouge import Rouge
from .cider.cider import CIDEr
from .spice.spice import Spice


class COCOEvaluation(object):
    def __init__(self, gold, silent=True):
        self.eval = {}
        self.example_scores = {}
        self.gold = gold
        self.silent = silent
        self.setup_tokenizer()
        self.setup_scorers()

    def setup_tokenizer(self):
        self.tokenizer = PTBTokenizer()

    def setup_scorers(self):
        self.scorers = [
            (BLEU(4), ["BLEU-1", "BLEU-2", "BLEU-3", "BLEU-4"]),
            (METEOR(),"METEOR"),
            (Rouge(), "ROUGE-L"),
            (CIDEr(), "CIDEr"),
            (Spice(silent=self.silent), "SPICE")
        ]

    def retrieve_examples(self, results):
        keys = results.getImgIds()
        gts, res = dict(), dict()
        for k in keys:
            gts[k] = self.gold.imgToAnns[k]
            res[k] = results.imgToAnns[k]
        return gts, res

    def evaluate(self, results):
        self.clear()
        gts, res = self.retrieve_examples(results)
        gts = self.tokenizer.tokenize(gts)
        res = self.tokenizer.tokenize(res)

        # =================================================
        # Compute scores
        # =================================================
        scorers = self.scorers
        for scorer, method in scorers:
            self.print('computing %s score...' % (scorer.method()))
            score, scores = scorer.compute_score(gts, res)
            if type(method) == list:
                for sc, scs, m in zip(score, scores, method):
                    self.set_eval(sc, m)
                    self.set_example_scores(scs, gts.keys(), m)
                    self.print("%s: %0.3f"%(m, sc))
            else:
                self.set_eval(score, method)
                self.set_example_scores(scores, gts.keys(), method)
                self.print("%s: %0.3f"%(method, score))
        
        return self.eval

    def set_eval(self, score, method):
        self.eval[method] = score

    def set_example_scores(self, scores, example_ids, method):
        for example_id, score in zip(example_ids, scores):
            if not example_id in self.example_scores:
                self.example_scores[example_id] = {}
                self.example_scores[example_id]["image_id"] = example_id
            self.example_scores[example_id][method] = score

    def print(self, text):
        if not self.silent:
            print(text)

    def clear(self):
        self.eval.clear()
        self.example_scores.clear()


class CommonGenEvaluation(COCOEvaluation):
    def retrieve_examples(self, results):
        keys = results.keys()
        gts, res = dict(), dict()
        for k in keys:
            gts[k] = self.gold[k]
            res[k] = results[k]
        return gts, res        