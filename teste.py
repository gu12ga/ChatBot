from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SuaClasse:
    def __init__(self, Questoes):
        self.Questoes = Questoes
        self.tfidf_vectorizer = TfidfVectorizer()
        self.X_tfidf = self.tfidf_vectorizer.fit_transform(self.Questoes)

    def getResposta(self, pergunta):
        nova_pergunta_tfidf = self.tfidf_vectorizer.transform([pergunta])

        # Calcular as similaridades de cosseno entre a nova pergunta e todas as questões
        similarities = cosine_similarity(nova_pergunta_tfidf, self.X_tfidf)

        # Obter os índices das questões mais semelhantes
        top_indices = similarities.argsort()[0][-10:][::-1]

        # Criar uma lista de tuplas com as 10 questões mais semelhantes, seus índices e valores de TF-IDF
        top_questions = []
        for i in top_indices:
            similarity_score = similarities[0][i]
            top_questions.append((self.Questoes[i], i, similarity_score))

        return top_questions

# Exemplo de uso:
questoes = [
    "Qual é a capital da França?",
    "Quanto é 2 + 2?",
    "Como está o clima hoje?",
    "Qual é o maior planeta do sistema solar?",
    "O que é a teoria da relatividade?",
    "Como cozinhar arroz?",
    "O que é a inteligência artificial?",
    "Quem escreveu 'Dom Quixote'?",
    "Como funciona a fotossíntese?",
    "Qual é a raiz quadrada de 16?"
]

sua_classe = SuaClasse(questoes)

pergunta = "Qual é a capital da França?"
resultados = sua_classe.getResposta(pergunta)

for i, (questao, indice, tfidf_similarity) in enumerate(resultados):
    print(f"{i+1}. Questão: {questao}")
    print(f"   Índice: {indice}")
    print(f"   Similaridade TF-IDF: {tfidf_similarity}")
