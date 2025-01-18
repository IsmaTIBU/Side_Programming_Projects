clear all;

m = 15
%Valeur de r pour les tests de simulink
r=1/200
Km_R = 0.3;
Beff = 1/80;
Jm = 1/100;
Jeff = Jm + (r^2)*m
e = 1/2;
K = (4*Jeff)/((e^2)*(Km_R))
Kd = ((4*Jeff)/(1/2) - Beff)/Km_R

%Liste de r pour les differents calculs a faire
r_list = [1/200, 1/30, 1]

Jeff_list = Jm + (r_list.^2)*m 

K_list = (4*Jeff_list)/((e.^2)*(Km_R))

Kd_list = ((4*Jeff_list)/(1/2) - Beff)/Km_R

Ti = 0.8


q2min =0.5;
q2max =1;
Dmin =[ m*q2min^2 0; 0 m ]
Dmax =[ m*q2max^2 0; 0 m ]

Jeff1min = Jm+r_list*Dmin(1 ,1)
Jeff1max = Jm+r_list*Dmax(1 ,1)
Jeff2min = Jm+r_list*Dmin(2 ,2)
Jeff2max = Jm+r_list*Dmax(2 ,2)