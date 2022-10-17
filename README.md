# rasa_project
Projeto final do curso de linguagem Natural.


# Instalação do Rasa Open Source

Mais simples de instalar impossível, através do comando pip abaixo tudo vai ficar pronto para começar a brincadeira.
```
pip3 install rasa
```
Após a instalação, podemos verificar se o Rasa foi instalado corretamente através do comando.

Versão Utilizada
```
rasa --version
```
Rasa Version      :         3.2.10

Minimum Compatible Version: 3.0.0 

Rasa SDK Version  :         3.2.2 

Python Version    :         3.8.10

Operating System  :         Windows-10-10.0.19044-SP0   



# Rasa Command Line Interface
O rasa possui uma série de comandos para que seja possível, configurar, treinar e testar o nosso chatbot. Abaixo uma relação extraída da documentação do próprio Rasa. Mas vamos por partes, aqui só vamos ver alguns desses comandos.

Rasa Command Line Interface:


<table>
<thead>
<tr>
<th>Command</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rasa init</code></td>
<td>Creates a new project with example training data, actions, and config files.</td>
</tr>
<tr>
<td><code>rasa train</code></td>
<td>Trains a model using your NLU data and stories, saves trained model in <code>./models</code>.</td>
</tr>
<tr>
<td><code>rasa interactive</code></td>
<td>Starts an interactive learning session to create new training data by chatting to your assistant.</td>
</tr>
<tr>
<td><code>rasa shell</code></td>
<td>Loads your trained model and lets you talk to your assistant on the command line.</td>
</tr>
<tr>
<td><code>rasa run</code></td>
<td>Starts a server with your trained model.</td>
</tr>
<tr>
<td><code>rasa run actions</code></td>
<td>Starts an action server using the Rasa SDK.</td>
</tr>
<tr>
<td><code>rasa visualize</code></td>
<td>Generates a visual representation of your stories.</td>
</tr>
<tr>
<td><code>rasa test</code></td>
<td>Tests a trained Rasa model on any files starting with <code>test_</code>.</td>
</tr>
<tr>
<td><code>rasa data split nlu</code></td>
<td>Performs a 80/20 split of your NLU training data.</td>
</tr>
<tr>
<td><code>rasa data convert</code></td>
<td>Converts training data between different formats.</td>
</tr>
<tr>
<td><code>rasa data migrate</code></td>
<td>Migrates 2.0 domain to 3.0 format.</td>
</tr>
<tr>
<td><code>rasa data validate</code></td>
<td>Checks the domain, NLU and conversation data for inconsistencies.</td>
</tr>
<tr>
<td><code>rasa export</code></td>
<td>Exports conversations from a tracker store to an event broker.</td>
</tr>
<tr>
<td><code>rasa evaluate markers</code></td>
<td>Extracts markers from an existing tracker store.</td>
</tr>
<tr>
<td><code>rasa -h</code></td>
<td>Shows all available commands.</td>
</tr>
</tbody>
</table>
