# src/agent.py
"""
Agent IA principal DataBot.
"""

import pandas as pd
from datetime import datetime
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_mistralai import ChatMistralAI

from src.tools.data_analyzer import DataAnalyzer
from src.tools.report_generator import ReportGenerator
from src.tools.chart_tools import ChartGenerator

class DataBot:
    """Agent IA assistant commercial"""
    
    def __init__(self, api_key=None, model="mistral-small-latest"):
        """
        Initialise DataBot.
        
        Args:
            api_key: Clé API Mistral (optionnel si dans .env)
            model: Modèle à utiliser
        """
        # Initialiser les outils
        self.data_analyzer = DataAnalyzer()
        self.report_generator = ReportGenerator()
        self.chart_generator = ChartGenerator()
        
        # Configurer le LLM
        self.llm = ChatMistralAI(
            model=model,
            temperature=0.1,
            mistral_api_key=api_key or self._get_api_key()
        )
        
        # Créer les outils LangChain
        self.tools = self._create_tools()
        
        # Créer l'agent
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False,
            max_iterations=3,
            handle_parsing_errors=True
        )
    
    def _get_api_key(self):
        """Récupère la clé API depuis les variables d'environnement"""
        import os
        return os.getenv("MISTRAL_API_KEY")
    
    def _create_tools(self):
        """Crée les outils LangChain"""
        return [
            Tool(
                name="AnalyseurDonnees",
                func=self.data_analyzer.analyze,
                description="Analyse les données de vente, produits, CA, stocks"
            ),
            Tool(
                name="GenerateurRapports",
                func=self.report_generator.generate,
                description="Génère des rapports commerciaux détaillés"
            ),
            Tool(
                name="GenerateurGraphiques",
                func=self.chart_generator.create_chart,
                description="Crée des graphiques à partir des données"
            )
        ]
    
    def ask(self, question):
        """
        Pose une question à DataBot.
        
        Args:
            question: Question en français
            
        Returns:
            Réponse de l'agent
        """
        try:
            response = self.agent.run(question)
            return response
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def analyze_file(self, file_path):
        """
        Analyse un fichier de données.
        
        Args:
            file_path: Chemin vers le fichier CSV
            
        Returns:
            Analyse des données
        """
        try:
            df = pd.read_csv(file_path)
            summary = self.data_analyzer.get_summary(df)
            return summary
        except Exception as e:
            return f"❌ Erreur lecture fichier: {str(e)}"

# Fonction simple pour utilisation rapide
def create_databot():
    """Crée une instance de DataBot (fonction de convenance)"""
    return DataBot()