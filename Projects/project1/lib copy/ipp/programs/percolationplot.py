# Accepts n (int) as command-line argument; and draws using standard draw a plot of the percolation
# probability (experimental observation) against the vacancy probability (control variable).

import estimate
import stddraw
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    stddraw.setCanvasSize(750, 750)
    stddraw.setXscale(-0.2, 1.2)
    stddraw.setYscale(-0.2, 1.2)
    stddraw.setPenRadius(0.0)
    stddraw.square(0.5, 0.5, 0.52)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledSquare(0.5, 0.5, 0.51)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(0.5, -0.1, 'Vacancy Probability')
    stddraw.text(-0.11, 0.5, 'Percolation')
    stddraw.text(-0.11, 0.45, 'Probability')
    _curve(n, 0.0, 0.0, 1.0, 1.0)
    stddraw.show()


# Plots the percolation curve (percolation probability vs vacancy probability) recursively.
def _curve(n, x0, y0, x1, y1, trials=10000, gap=0.01, error=0.0025):
    xm = (x0 + x1) / 2
    ym = (y0 + y1) / 2
    fxm = estimate.evaluate(n, xm, trials)
    if x1 - x0 < gap or abs(ym - fxm) < error:
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0)
        return
    _curve(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, 0.005)
    if 0.55 < xm < 0.6:
        xyLabel = '(' + str(round(xm, 3)) + ', ' + str(round(fxm, 3)) + ')'
        stddraw.text(xm + 0.1, fxm, xyLabel)
    stddraw.show(0)
    _curve(n, xm, fxm, x1, y1)


if __name__ == '__main__':
    main()
