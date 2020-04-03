import numpy as np
from friprove import friprove, plotfriprove
from propulsjonsprove import propulsjonsprove, printpropulsjon
from effektbehov import effektbehov, printeffektbehov, finnHastOgTurtall

def main():
    #------- Beregning og plotting av friprøvediagram -------
    Ktp_f, Ktd_f, Ktt_f, Kq_f, h0_f, J_f = friprove()
    plotfriprove(Ktp_f, Ktd_f, Ktt_f, Kq_f, h0_f, J_f)

    #------- Beregning av propulsjonskoeffisienter fra propulsjonsprøve -------
    V, J, Ktt, Kq, J0, Kq0, wm, hr, t, hh = propulsjonsprove(Ktt_f, Kq_f, J_f)
    printpropulsjon(V, J, Ktt, Kq, J0, Kq0, wm, hr, t, hh)

    #------- Beregning av fullskala effektbehov -------
    Vs, num, Jstar, Kqstar, rpm, Pd = effektbehov(Ktt_f, Kq_f, J_f, wm, t, hr)
    printeffektbehov(Vs, Jstar, Kqstar, rpm, Pd)

    #------ Vise grafisk løsning av turtall og hastighet ------
    finnHastOgTurtall(Vs, rpm, Pd)
main()