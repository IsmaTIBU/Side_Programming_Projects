clc;
clear all;

cas_d_etude = 1;  % Índice de la sección considerada
plot_p = 0;       % Si es 1, produce un gráfico; si es 0, no

N = 10000;  % Número de experiencias a ejecutar
echantillons_Z = [];  % Vector para almacenar las muestras

% Ejecutar múltiples experiencias y almacenar los resultados
for index = 1:N
    [Z, L, m, H, Hfull, bar_v, C_v, x] = simulationDonnees(cas_d_etude, plot_p);
    % Almacenar las realizaciones de Z en echantillons_Z
    echantillons_Z = [echantillons_Z, Z];
end

% Calcular la desviación estándar (σ) de las muestras obtenidas
sigma = std(echantillons_Z);

% Mostrar el valor de σ
fprintf('La valeur de σ est : %.4f\n', sigma);

% Graficar las realizaciones de Z (opcional)
figure;
hold on;
grid on;
for i = 1:2:length(echantillons_Z)
    plot(echantillons_Z(i), echantillons_Z(i+1), 'bo');
end

