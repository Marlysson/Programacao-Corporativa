## Validação 1

```
\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}
```

Ex: CNPJ: Ex.: 15.123.321/8883-22

## Validação 2

```
(\d{3}\.?){2}\d{3}-?\d{2}
```

Ex: CPF: 002.919.190-55 ou 002919160-50 ou ainda 00291916446

## Validação 3

Endereço IP: Ex.: 192.168.2.1

## Validação 4

```
[A-Z]{3}[.-]{1}\d{4}
```

Ex: Placa Veículo: OEG-7118

## Validação 5
```
\(?(?P<ddd>\d{2})\)?[- ](\d{9}|\d{3,5})-?\d{4}  ( with flags /gm )
```

Ex: Telefones:

(32) 225-1920
86-99975-0202
(86) 3221-1920
86-032211313

## Validação 6
```
^[a-z_\d-]{1,8}$
```
Requisitos: Validação de usuário: só pode conter com letras minúsculas. E ter no máximo 8
caracteres: podendo ser números, underlines e traços

Validação 7

```
^(?P<horas>[01]{1}[0-9]|2[0-3])h(?P<minutos>[0-5][0-9])min(?P<segundos>[0-5][0-9])s$
```

Formato: 19h32min16s