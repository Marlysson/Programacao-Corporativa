## Validação 1

> Ex: CNPJ: 15.123.321/8883-22

```
\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}
```

## Validação 2

> Ex: CPF
- 002.919.190-55
- 002919160-50
- 00291916446

```
(\d{3}\.?){2}\d{3}-?\d{2}
```

## Validação 3

> Endereço IP: Ex.: 192.168.2.1

**PENDENTE**

## Validação 4

>Ex: Placa Veículo
- OEG-7118
- OEG.7118

```
[A-Z]{3}[.-]{1}\d{4}
```

## Validação 5

>Ex: Telefones:
- (32) 225-1920
- 86-99975-0202
- (86) 3221-1920
- 86-032211313

```
\(?(?P<ddd>\d{2})\)?[- ](\d{9}|\d{3,5})-?\d{4}  ( with flags /gm )
```

## Validação 6
> Validação de usuário: só pode conter com letras minúsculas. E ter no máximo 8
caracteres: podendo ser números, underlines e traços

```
^[a-z_\d-]{1,8}$
```

## Validação 7

> Formato: 19h32min16s

```
^(?P<horas>[01]{1}[0-9]|2[0-3])h(?P<minutos>[0-5][0-9])min(?P<segundos>[0-5][0-9])s$
```

##Validação 8

> Ex:
1. 10/10/2016
2. 10/Jan/2016
3. 10 de Janeiro de 2016

#### Validação do formato 1

>10/10/2006

```
(?P<dia>0[1-9]|[12][0-9]|3[01])\/
(?P<mes>0[1-9]|1[0-2])\/
(?P<ano>19([0]{2}|\d{2})|2\d{3})
```

#### Validação do formato 2

>10/Jan/2016

```
(?P<dia>0[1-9]|[12][0-9]|3[01])\/
(?P<mes>[A-Z][a-z]{2})\/
(?P<ano>19([0]{2}|\d{2})|2\d{3})
```

#### Validação do formato 3

>10 de Janeiro de 2016

```
(?P<dia>0[1-9]|[12][0-9]|3[01]) de (?P<mes>[A-Z][a-z]{1,8}) de (?P<ano>19([0]{2}|\d{2})|2\d{3})
```