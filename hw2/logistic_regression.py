__author__ = 'manuelli'
import numpy as np


class LogisticRegression:

    def __init__(self, x, y):
        self.N = np.size(self.y)
        self.y = np.reshape(y,(self.N,))
        self.x = x
        self.d = np.shape(x)[1] # this is the size of w
        # pad with ones at the beginning
        self.x_full = np.zeros((N,d+1))
        self.x_full[:,0] = np.zeros(N)
        self.x_full[:,1:] = self.x



    def NLL(self,w_full):
        w_0 = w_full[0]
        w = w_full[1:]
        exponent = -1.0*numpy.multiply(self.y, np.dot(self.x, w) + w_0)
        nll = np.sum(np.log(1.0 + np.exp(exponent)))

        return nll

    def NLL_Reg(self, w_full, lam):
        w = w_full[1:]
        return self.NLL(w_full) + lam*np.norm(w)

    # computes the gradient of NLL, not the regularization term though
    def NLL_grad(self, w_full):
        exponent = -1.0*numpy.multiply(self.y, np.dot(self.x, w) + w_0)
        t = np.log(1.0 + np.exp(exponent))
        t_inv = np.power(t,-1) # this is N x 1
        a = -1.0*np.multiply(self.y[:,None], self.x_full) # this is -y x_full = N x (d+1)
        grad = np.multiply(t_inv[:,None], a) # this is N x (d+1)
        grad = np.sum(grad, axis=0) # need to take column sum, now grad should be d x 1
        return grad

    # computes the gradient for the full regularized NLL objective
    def NLL_Reg_grad(self, w_full, lam):
        nllGrad = self.NLL_grad(w_full)
        regGrad = 2.0*lam*w_full # this is the gradient for the regularizer term
        regGrad[0] = 0
        return nllGrad + regGrad



    def predict(self, w_full, x):
        w_0 = w_full[0]
        w = w[1:]

        val = w_0 + np.dot(w,x)
        if (val > 0):
            return 1
        else:
            return 0

    def splitW(self,w_full):
        w_0 = w_full[0]
        w = w_full[1:]
        return (w_0,w)

    # compute the classification error rate for a given dataset
    def classificationErrorRate(self, w_full):

        (w_0,w) = self.splitW(w_full)
        val = w_0 + np.dot(self.x, w_full)
        val = np.multiply(y,val)

        # any entries in val that are < 0 are missclassified
        missclasified = np.size(val[val < 0])
        missclassifiedRate = missclasified/(self.N*1.0)

        return missclassifiedRate, missclasified



    @staticmethod
    def fromFile(file, type="train"):
        filename = "/hw2_resources/data/" + file + "_" + type + ".csv"
        train = loadtxt(filename)
        X = np.array(train[:,0:2])
        Y = np.array(train[:,2:3])
        lr = LogisticRegression(X,Y)

        return lr







