if __name__=='__main__':

    import math
    import random

    N = [10, 100, 1000, 1000000]

    for i in range(len(N)):
        a = 0
        for j in range(N[i]):
            x = random.random()
            y = random.random()
            if (x*x + y*y) < 1:
                a = a + 1
        pi_approx = 4*a/N[i]
        print('for N= '+str(N[i])+': approx pi: '+str(pi_approx)+ ', absolute error: '+str(abs(math.pi - pi_approx))+ ', relative error: '+str((abs(math.pi - pi_approx))/math.pi))

