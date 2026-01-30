#!/usr/bin/env python3
"""
DataBot - Point d'entrée principal
Assistant IA pour l'analyse commerciale
"""

import sys
import argparse
from pathlib import Path

# Ajouter le dossier courant au path
sys.path.insert(0, str(Path(__file__).parent))

from src.agent import DataBot
from src.utils.config import Config
from src.utils.logger import setup_logger
from src.tools.data_analyzer import DataAnalyzer


def print_banner():
    """Affiche la bannière d'introduction"""
    banner = """
    ╔══════════════════════════════════════════════════════╗
    ║                    🤖 DataBot v1.0                   ║
    ║       Assistant IA d'Analyse Commerciale             ║
    ║       Projet de Fin d'Études - Génie Informatique    ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)


def interactive_mode():
    """Mode interactif ligne de commande"""
    print_banner()
    print("🔧 Initialisation de DataBot...")
    
    try:
        # Configuration
        config = Config()
        logger = setup_logger("databot")
        
        # Création de l'agent
        print("🧠 Chargement de l'agent IA...")
        bot = DataBot(api_key=config.mistral_api_key)
        
        print("✅ DataBot est prêt !")
        print("\n💬 Mode interactif - Tapez 'quit' pour sortir")
        print("=" * 60)
        
        # Boucle de conversation
        conversation_count = 0
        while True:
            try:
                # Input utilisateur
                question = input(f"\n[Q{conversation_count + 1}] 👤 Vous: ").strip()
                
                if question.lower() in ['quit', 'exit', 'q', 'bye']:
                    print("\n👋 Au revoir ! Merci d'avoir utilisé DataBot.")
                    break
                
                if not question:
                    continue
                
                # Traitement
                print("🤖 DataBot analyse...")
                response = bot.ask(question)
                
                # Affichage réponse
                print(f"\n📊 Réponse:")
                print("-" * 40)
                print(response)
                print("-" * 40)
                
                # Log
                logger.info(f"Question: {question[:50]}...")
                conversation_count += 1
                
            except KeyboardInterrupt:
                print("\n\n⏹️  Interruption. Au revoir !")
                break
            except Exception as e:
                print(f"❌ Erreur: {str(e)}")
                logger.error(f"Erreur: {str(e)}")
        
        # Statistiques
        print(f"\n📈 Session terminée:")
        print(f"   • Questions traitées: {conversation_count}")
        print(f"   • Logs disponibles: logs/databot.log")
        
    except Exception as e:
        print(f"❌ Erreur d'initialisation: {str(e)}")
        sys.exit(1)


def analyze_file_mode(file_path):
    """Mode analyse de fichier"""
    print(f"📁 Analyse du fichier: {file_path}")
    
    try:
        analyzer = DataAnalyzer()
        results = analyzer.analyze_csv(file_path)
        
        print("\n📊 RÉSULTATS DE L'ANALYSE:")
        print("=" * 60)
        
        if results.get("success"):
            stats = results.get("statistics", {})
            
            print(f"✅ Fichier analysé avec succès")
            print(f"   • Lignes: {stats.get('row_count', 0)}")
            print(f"   • Colonnes: {stats.get('column_count', 0)}")
            print(f"   • Données: {stats.get('period', 'N/A')}")
            
            if "insights" in results:
                print("\n💡 INSIGHTS:")
                for insight in results["insights"][:3]:  # Top 3 insights
                    print(f"   • {insight}")
                    
        else:
            print(f"❌ Erreur: {results.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"❌ Erreur d'analyse: {str(e)}")


def generate_report_mode(output_dir="reports"):
    """Mode génération de rapport"""
    print(f"📋 Génération de rapport dans: {output_dir}")
    
    try:
        from src.tools.report_generator import ReportGenerator
        
        generator = ReportGenerator()
        report_path = generator.generate_comprehensive_report(output_dir)
        
        print(f"\n✅ Rapport généré:")
        print(f"   📄 Fichier: {report_path}")
        print(f"   📁 Dossier: {output_dir}")
        
    except Exception as e:
        print(f"❌ Erreur génération rapport: {str(e)}")


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(
        description="DataBot - Assistant IA d'analyse commerciale",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  %(prog)s                    # Mode interactif
  %(prog)s --file ventes.csv  # Analyse de fichier
  %(prog)s --report           # Génération de rapport
  %(prog)s --version          # Version du programme
        """
    )
    
    parser.add_argument(
        "-f", "--file",
        help="Analyser un fichier CSV",
        metavar="FILE"
    )
    
    parser.add_argument(
        "-r", "--report",
        action="store_true",
        help="Générer un rapport complet"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="DataBot v1.0.0 - Projet de Fin d'Études"
    )
    
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Mode debug"
    )
    
    args = parser.parse_args()
    
    # Exécution selon les arguments
    if args.file:
        analyze_file_mode(args.file)
    elif args.report:
        generate_report_mode()
    else:
        interactive_mode()


if __name__ == "__main__":
    main()