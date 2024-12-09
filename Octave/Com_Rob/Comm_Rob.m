clear all
#Q.4
#a
Km_R=0.3;
Beff=1/80;
Jm=1/100;
r=[1/200, 1/30, 1];
res=zeros(2,length(r));
m=15;
Jeff=Jm+(r.^2)*m;
err_tet=1/2;
K=(4*Jeff/err_tet^2)/Km_R;
Kd=((4*Jeff/err_tet)-Beff)/Km_R;
K
Kd

% Visualizar resultados
disp("Resultados:");
disp(table(r', Jeff', K', Kd', 'VariableNames', {'r', 'Jeff', 'K', 'Kd'}));

% Trazar los lugares de las raíces
figure;
for i = 1:length(r)
    r = r(i);

    % Sistema antes de corrección
    num_before = [1];
    den_before = [Jeff(i), Beff, 0];
    system_before = tf(num_before, den_before);

    % Sistema después de corrección
    num_after = [K(i) * Km_R, Kd(i) * Km_R];
    den_after = [Jeff(i), (Beff + Kd(i) * Km_R), K(i) * Km_R];
    system_after = tf(num_after, den_after);

    % Tracé del lugar de las raíces
    subplot(1, length(r), i);
    rlocus(system_before);
    hold on;
    rlocus(system_after);
    title(['r = ', num2str(r)]);
    legend('Antes', 'Después');
    grid on;
end
