<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Curso de PHP - CursoEmVideo.com</title>
</head>
<body>
    <?php
    /* Esse exercvido pretente demostrar
    o uso de operadores aouso de operadores
    e decremento*/
        $atual = $_GET["aa"]; // Essa linha vai pegar o ano na url
        echo "O Ano atual é $atual </br> E o ano anterior e ".--$atual;
    ?>
</body>
</html>
