<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Funções Aritimeticas em PHP</title>
    <style>
        <h2 {
            font: 10pt Arial;
            color: cornflowerblue;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <?php
        $v1 = $_GET["x"];
        $v2 = $_GET["y"];
        echo "<h2>Valores recebidos: $v1 e $v2</h2>";
        echo "O valor absoluto de $v2 é ".abs($v2);
        echo "</br>o valor de $v1<sup>$v2</sup> é " . pow($v1, $v2);
        echo "</br> A raiz de $v1 é ". sqrt($v1);
        echo "</br> O Valor de $v2 arredondado é ".round($v2); // ceil floor
        echo "</br> A parte inteira de $v2 é ".intval($v2);
        echo " </br> o valor de $v1 em moeda é R$".number_format($v1,2,",",".");
    ?>
</body>
</html>