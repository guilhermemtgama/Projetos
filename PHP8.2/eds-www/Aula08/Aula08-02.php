<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Curso de PHP - CursoEmVideo.com</title>
</head>
<body>
    <?php
        $nome = isset($_GET["nome"])?$_GET["nome"]:"Nao foi informado";
        $ano = isset($_GET["ano"])?$_GET["ano"]:"Nao foi informado";
        $sexo = isset($_GET["sexo"])?$_GET["sexo"]:"sem sexo";
        $idade = date("Y") - $ano;
        echo "$nome é $sexo e tem $idade anos."
    ?>
    <a href="Aula08-02.html">Voltar</a>
</body>
</html>
