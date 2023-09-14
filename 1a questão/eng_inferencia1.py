# Base de conhecimento 
knowledge_base_q1 = {
    'é mamífero': {
        'é carnívoro': {
            'tem cor amarelo-tostado': {
                'tem manchas escuras': 'leopardo',
                'tem listras pretas': 'tigre'
            }
        },
        'é ungulado': {
            'tem pernas longas': {
                'tem pescoço comprido': {
                    'tem cor amarelo-tostado': {
                        'tem manchas escuras': 'girafa'
                    }
                }
            },
            'tem cor branca': {
                'tem listras pretas': 'zebra'
            }
        },
        'voa': {
            "não é uma ave": 'morcego'
        }
    },
    'é uma ave': {
        'voa': {
            'é um bom voador': 'albatroz',
            'tem pernas longas': {
                'tem pescoço comprido': {
                    'tem cauda curta': {
                        'é cor de rosa': 'flamingo'
                    }
                }
            }
        },
        'não voa': {
            'nada': {
                'é preto e branco': 'pinguim'
            },
            'tem pernas longas': {
                'tem pescoço comprido': {
                    'é preto e branco': 'avestruz'
                }
            },
            'tem corpo arredondado': {
                'tem penas densas': {
                    'não voa': {
                        'é doméstico': 'galinha'
                    }
                }
            }
        }
    }
}


class AnimalClassifier:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.previous_nodes = []

    def ask_question(self, question):
        while True:
            user_input = input(question + " (sim/não/voltar/por que): ").lower()
            if user_input == 'sim':
                self.previous_nodes.append(f"{question} = Sim")
                return "sim"
            elif user_input == 'não':
                self.previous_nodes.append(f"{question} = Não")
                return "não"
            elif user_input == 'voltar':
                return "voltar"
            elif user_input == 'por que':
                self.previous_nodes.append(f"{question} = Por que?")
                return "por que"
            else:
                print("Por favor, responda com 'sim', 'não', 'voltar' ou 'por que'.")

    def infer(self, current_node, path=None):
      if path is None:
          path = []

      skip_question = False  # Flag para controlar se deve pular a próxima pergunta

      while True:
          if isinstance(current_node, dict):
              for question, next_nodes in list(current_node.items()):
                  if skip_question:
                      skip_question = False  # Redefinindo a flag para a próxima pergunta
                      continue  # Pule a pergunta atual
                  response = self.ask_question(f"O animal {question}?")
                  if response != "por que":
                    path.append(f"{question} = {response}")
                  if response == "sim":
                      return self.infer(next_nodes, path)
                  elif response == "não":
                      path.append(f"{question} = {response}")
                      path.pop()
                  elif response == "por que":
                      final_node = self.get_final_node(current_node, path)
                      self.display_explanation(path, final_node, current_node, next_nodes)
                      skip_question = True
          else:
                print(f"O animal que você está pensando é um {current_node}.")
                return


    #Função funcionando corretamente
    def get_final_node(self, current_node, path):
      temp_path = path.copy()  # Crie uma cópia temporária do caminho
      temp_node = current_node
      for item in temp_path:
          question, response = item.split(' = ')
          #print(f'{question} e {response}')
          if question in temp_node:
              if response == 'sim':
                  temp_node = temp_node[question].get('sim', {})
              elif response == 'não':
                  #print(temp_node[question])
                  temp_path.pop()  # Remova a última pergunta da cópia temporária do caminho
                  temp_node.pop(question, None)
                  #print(temp_node)
      if isinstance(temp_node, dict):
          for key, value in temp_node.items():
              if isinstance(value, str):
                  return value
      return temp_node.items(0)

    #função para mostrar o "por que"
    def display_explanation(self, path, final_node, current_node, next_node):
      print("\nPara concluir:")
      print(f" - {final_node} = Sim")
      print(f"Eu preciso saber se:")
      for item in path:
          question = item.split(' = ')[0]
          response = item.split(' = ')[-1]
          if(response != "não"):
            print(f" - {question} = {response}")

      print(f"==> {list(current_node.keys())[0]} = Sim")

      while next_node:
          if isinstance(next_node, dict):
              for question, response in list(next_node.items()):
                print(f" - {question} = Sim")
                current_node = next_node
                next_node = response
          else:
            return


    def run(self):
        while True:
            print("Pense em um animal e eu vou tentar adivinhar qual é!")
            self.infer(self.knowledge_base)

            while True:
                replay_choice = input("\nEscolha uma opção:\n(j) Jogar novamente\n(r) Ver como chegou ao resultado\n(s) Encerrar o jogo\nEscolha uma opção: ").lower()
                if replay_choice == 'j':
                    break
                elif replay_choice == 'r':
                    self.show_history()
                elif replay_choice == 's':
                    print("Obrigado por jogar! Até a próxima.")
                    return
                else:
                    print("Opção inválida. Por favor, escolha 'j' para jogar novamente, 'r' para ver o histórico ou 's' para sair.")

    def show_history(self):
        print("\nHistórico de perguntas e respostas:")
        for item in self.previous_nodes:
                print(item)

game = AnimalClassifier(knowledge_base_q1)
game.run()