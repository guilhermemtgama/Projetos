<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Curso de PHP - CursoEmVideo.com</title>
</head>
<body>
    <?php
        $nota1 = $_GET["n1"];
        $nota2 = $_GET["n2"];
        $m = ($nota1+$nota2)/2;
        echo "a media entre $nota1 e $nota2 e $m <br/>";
        echo "a situacao do aluno e ".(($m < 6)?"<H6>REPROVADO<H6/>":"<H6>APROVADO<H6/>");

    ?>
</body>
</html>
