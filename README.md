# G11-Controle-de-Estacionamento-OO
## TRABALHO PRÁTICO DE OO - CONTROLE DE ESTACINAMENTO

    Grupo: 11
    Nome: Arthur Faria Campos  Matricula: 16/0024242

### Diagrama de Classes

Aqui estão as principais classes do nosso Sistema de Estacionamento:

* **ParkingLot:** A parte central da organização para a qual este software foi projetado. Possui
  atributos como "Nome" para distingui-lo de quaisquer outros estacionamentos e "Endereço" para
  definir sua localização.
* **Account:** Teremos dois tipos de contas no sistema: uma para Atendente de estacionamento e outra
  para Cliente .
* **Parking Ticket** Esta classe incluirá um bilhete de estacionamento. Os clientes irão tirar um
  tíquete ao entrar no estacionamento.
* **Veículo:** Os cadastros de cada veículos que ficarão estacionados nas vagas.
* **EntryPanel e ExitPanel:** EntryPanel imprimirá os tíquete, e ExitPanel facilitará o pagamento da
  taxa de ingresso.
* **Payment:** Esta classe será responsável pelo pagamento. O sistema suportará transações com
  cartão de crédito e dinheiro.
* **Park Rate:** Esta classe manterá o controle das taxas de estacionamento por hora. Ele
  especificará um valor em dólar para cada hora.

<p align="center">
    <img src="/media/estacionamento_UML.png" alt="Parking Lot UML">
    <br />
    UML do Estacionamento
</p>

### Uso de caso

Aqui estão os principais atores em nosso sistema:

* **Admin:** Principalmente responsável por adicionar e modificar estacionamento, aumentar/diminuir
  vagas, adicionar/remover atendentes de estacionamento, etc.
* **Cliente** Todos os clientes podem obter um tíquete de estacionamento e pagar por ele.
* **Atendente de estacionamento** Os atendentes de estacionamento podem fazer todas as atividades em
  nome do cliente e podem receber dinheiro para o pagamento do tíquete.


Aqui estão os principais casos de uso para estacionamento:

* **Adicionar / Remover / Editar uma vaga de estacionamento:** Para adicionar, remover ou modificar
  uma vaga de estacionamento.
* **Adicionar / Remover um atendente de estacionamento:** Para adicionar ou remover um atendente de
  estacionamento do sistema.
* **Gerar o tíquete:** Para fornecer aos clientes um novo tíquete de estacionamento ao entrar no
  estacionamento.
* **Pagar o tíquete:** Para digitalizar um tíquete para descobrir a taxa total.
* **Pagamento com cartão de crédito:** Para pagar com cartão de crédito.
* **Pagamento à vista:** Para pagar em dinheiro.
* **Adicionar / modificar taxa de estacionamento:** Para permitir que o administrador adicione ou
  modifique a taxa de estacionamento por hora.

### Code

A seguir está a estrutura de código básico para o nosso sistema de estacionamento:

**Enums e Data Types:** Aqui estão os tipos comuns  necessários para o codigo:

```python
# common.py
from enum import Enum
```

**ParkingRate:** O sistema de taxas do estacionamento

```python
# parking_rate.py
from .common import *

class ParkingRate:
    None

```

**ParkingLot:** O systema so tera uma classe dessa.

```python
# parking_lot.py
from .common import *

class ParkingLot:

    def __init__(self, name, address):
        None

    def getNewParkingTicket(self, vehicle):
        None

    def isFull(self):
        None

```

**EntryPanel e ExitPanel:** Classe para gerar e pagar o tíquete do estacionamento:

```python
# panels.py
from .common import *
from .parking_lot import *

class EntryPanel:
    None

class ExitPanel:
    None

```



**Account, Customer, Admin, and ParkingAttendant:** Usuarios do sistema:

```python
# account_types.py
from .common import *

class Account:
    None

class Customer:
    None

class ParkingAttendant:
    None

class Admin:
    None

```
**Vehicle:** Classe dos dados de veiculos.

```python
# parking_interface.py
from .common import *

class Vehicle:
    None

```
**Payment:** Classe para pagamento

```python
# payment.py
from .common import *

class Payment:
    None

class CreditCardTransaction:
    None

class CashTransaction:
    None

```

**ParkingInterface:** Construção da interface grafica para utilização do sistema.

```python
# parking_interface.py
from .common import *

```

