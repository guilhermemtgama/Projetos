<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Curso de PHP - CursoEmVideo.com</title>
</head>
<body>
    <?php
        $ano = $_GET["an"];
        $idade = 2023 - $ano;
        echo "Quem nasceu em $ano tem a idade de $idade anos.<br/>";
        $tipo = ($idade >=18 && $idade <65)?"OBRIGATORIO":"NAO OBRIGATORIO";
        echo " E dessa forma seu voto e $tipo"

    ?>
</body>
</html>
