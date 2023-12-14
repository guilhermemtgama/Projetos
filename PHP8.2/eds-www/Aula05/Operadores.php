<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Somadores</title>
</head>
<body>
    <?php
        $n1 = $_GET["a"];
        $n2 = $_GET["b"];
        echo  "<h2>Valores Recebidos: $n1 e $n2</h2>";
        $media = ($n1+$n2) / 2;
        echo "A soma vale ".($n1+$n2);
        echo "<br/>A subtraçao vale ".($n1-$n2);
        echo "<br/>A multiplicação vale ".($n1*$n2);
        echo "<br/>A divisao vale ".($n2/$n1);
        echo "<br/>A modulo vale ".($n1%$n2);
        echo "<br/>A media dos valores é $media"
    ?>
</body>
</html>
