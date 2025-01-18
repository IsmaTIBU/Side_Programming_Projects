clc;
clear all;

cas_d_etude = 1;  % Indice de la section considérée
plot_p = 0;       % Si égal à 1, produit un graphique ; si égal à 0, aucun graphique

N = 500;  % Nombre d'expériences à exécuter
echantillons_Z = [];  % Vecteur pour stocker les échantillons

% Exécuter plusieurs expériences et stocker les résultats
for index = 1:N
    [Z, L, m, H, Hfull, bar_v, C_v, x] = simulationDonnees(cas_d_etude, plot_p);
    % Stocker les réalisations de Z dans echantillons_Z
    echantillons_Z = [echantillons_Z, Z];
end

% Calculer l'écart-type (σ) des échantillons obtenus
sigma = std(echantillons_Z);

% Tracer les réalisations de Z sous forme de points (tous en bleu)
figure;
hold on;
grid on;
axis equal;

colors = lines(L); % Palette de couleurs pour les ellipses

for l = 1:L
    % Extraire les points pour l'amère l
    points_x = echantillons_Z(2*l-1, :);
    points_y = echantillons_Z(2*l, :);

    % Tracer les points de l'amère l
    scatter(points_x, points_y, 10, 'b', 'filled', 'MarkerFaceAlpha', 0.5);

    % Calculer la moyenne (mx) et la covariance (Px) des points
    mx = mean([points_x; points_y], 2); % Moyenne des points (2x1)
    Px = C_v((2*l-1):(2*l), (2*l-1):(2*l));     % Matrice de covariance (2x2)

    % Tracer l'ellipse autour des points de l'amère l
    ellipse(mx, Px, colors(l, :)); % Ajouter l'ellipse avec la couleur correspondante
end

title('Distribution des réalisations de Z avec ellipses');
xlabel('Composante Z_{x}');
ylabel('Composante Z_{y}');
hold off;

