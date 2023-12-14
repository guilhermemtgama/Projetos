<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Curso de PHP - CursoEmVideo.com</title>
</head>
<body>
    <?php
        $a = 3;
        $b = &$a;
        $b +=5;
        echo "A variavel A vale $a";
        echo "<br/> A variavel B vale $b";
    ?>
</body>
</html>
