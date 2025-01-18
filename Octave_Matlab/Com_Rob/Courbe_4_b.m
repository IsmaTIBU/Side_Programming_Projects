%Courbe de question 4.b


% Système en boucle ouverte
num = [r*Km_R]; % Numérateur
den = [Jeff Beff]; % Dénominateur
sys_open = tf(num, den);

% Lieu des racines en boucle ouverte
figure;
rlocus(sys_open);
title('Lieu des racines en boucle ouverte');

% Marges de stabilité
figure;
margin(sys_open);
title('Marges de stabilité avant correction');