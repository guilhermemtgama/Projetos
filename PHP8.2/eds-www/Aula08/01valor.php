<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Curso de PHP - CursoEmVideo.com</title>
</head>
<body>
    <?php
        $valor=$_GET["v"];
        $rq = sqrt($valor);
        echo "A raiz de $valor é igual a $rq".number_format($rq,2);
    ?>
    <a href="Aula08.html">Voltar</a>
</body>
</html>