def Converter():
    n=int(input('Enter Number of Revolution:'))
    v=int(input('Enter Number of Min:'))
    c=int(input('Enter Radious:'))
    RPM= n / v
    RPS=RPM*0.10472
    MS=0.1047*c*RPM
    Hz=RPM/60
    print('Rev Per Min',RPM)
    print('Radian Per Sec',RPS)
    print('RPM TO M/s',MS)
    print('RPM TO Hz',Hz)