function calculoRebotePared(incidentAngleInRadians, wallType) {
    let reflectedAngleInRadians;

    if (wallType === 'vertical') {
        // Rebote en una pared vertical: el ángulo reflejado es -incidentAngleInRadians (reflexión horizontal)
        reflectedAngleInRadians = Math.atan2(Math.sin(incidentAngleInRadians), -Math.cos(incidentAngleInRadians));
    } else if (wallType === 'horizontal') {
        // Rebote en una pared horizontal: el ángulo reflejado es π - incidentAngleInRadians (reflexión vertical)
        reflectedAngleInRadians = Math.atan2(-Math.sin(incidentAngleInRadians), Math.cos(incidentAngleInRadians));
    } else {
        throw new Error('Tipo de pared no válido. Usa "vertical" u "horizontal".');
    }

    // Ajustamos el ángulo para que esté en el rango [0, 2π)
    if (reflectedAngleInRadians < 0) {
        reflectedAngleInRadians += 2 * Math.PI;
    }

    return reflectedAngleInRadians;
}
function calculaDistancia(x1, y1, x2, y2) {
    const dx = x2 - x1;
    const dy = y2 - y1;
    return Math.sqrt(dx * dx + dy * dy);
}
function anguloEntreDosPuntos(x1, y1, x2, y2) {
    const dx = x2 - x1;
    const dy = y2 - y1;
    return angleInRadians = Math.atan2(dy, dx);
    //const angleInDegrees = angleInRadians * (180 / Math.PI);
    //return angleInDegrees;
}