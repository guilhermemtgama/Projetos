<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Curso de PHP - CursoEmVideo.com</title>
</head>

<body>
    <?php
    $n = isset($_GET["num"]) ? $_GET["num"] : 0;
    $o = isset($_GET["Oper"]) ? $_GET["Oper"] : 1;
    switch ($o) {
        case 1:
            $r = $n * 2;
            break;
        case 2:
            $r = $n * $n * $n;
            break;
        case 3:
            $r = sqrt($n);
    }
    echo "O resultado da operação solicitada foi $r"
    ?><br />
    <a href="Exercicio1.html">Voltar</a>
</body>

</html>