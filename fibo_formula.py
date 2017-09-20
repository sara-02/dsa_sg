from math import sqrt


class NthFibonacciNumber(object):

    def __init__(self):
        self.sqrt_5 = sqrt(5)
        self.base_positive = (1 + self.sqrt_5) / 2
        self.base_negative = (1 - self.sqrt_5) / 2

    def get_nth_fibo_number(self, nth):
        return int((self.base_positive**nth - self.base_negative**nth) / self.sqrt_5)

    def print_nth_fibo_number(self, nth):
        if nth < 0:
            print "Fibonacci not possible"
            return
        if nth == 0:
            print "0th Fibonacci number is =  0"
            return
        if nth == 1:
            print "1st Fibonacci number is =  1"
            return
        if nth == 2:
            print "2nd Fibonacci number is =  2"
            return
        suffix = "th"
        if nth == 3:
            suffix = "rd"
        number = self.get_nth_fibo_number(nth)
        print "The %d%s Fibonacci number is =  %d" % (nth, suffix, number)


if __name__ == '__main__':
    fn = NthFibonacciNumber()
    fn.print_nth_fibo_number(5)
    fn.print_nth_fibo_number(13)
    fn.print_nth_fibo_number(-9)
    fn.print_nth_fibo_number(1)
