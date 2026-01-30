# modules/memory_manager.py - VERSION STANDALONE SANS LANGCHAIN
"""
Gestionnaire de mémoire simple pour DataBot.
Ne dépend d'aucune bibliothèque externe.
"""

import json
from datetime import datetime
from typing import List, Dict, Any, Optional

class MemoryManager:
    """Gestionnaire de mémoire ultra-simple pour DataBot"""
    
    def __init__(self, max_messages: int = 20):
        """
        Initialise le gestionnaire de mémoire.
        
        Args:
            max_messages: Nombre maximum de messages à conserver
        """
        self.history: List[Dict[str, Any]] = []
        self.max_messages = max_messages
        print(f"🧠 MemoryManager initialisé (max: {max_messages} messages)")
    
    def add_message(self, role: str, content: str) -> None:
        """
        Ajoute un message à l'historique.
        
        Args:
            role: 'human' pour utilisateur, 'ai' pour assistant
            content: Contenu du message
        """
        if role not in ['human', 'ai']:
            role = 'human'  # Valeur par défaut
        
        message = {
            "role": role,
            "content": str(content),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.history.append(message)
        
        # Limite la taille de l'historique
        if len(self.history) > self.max_messages:
            self.history = self.history[-self.max_messages:]
    
    def add_conversation(self, question: str, answer: str) -> None:
        """
        Ajoute une paire question/réponse.
        
        Args:
            question: Question de l'utilisateur
            answer: Réponse de l'assistant
        """
        self.add_message("human", question)
        self.add_message("ai", answer)
        print(f"💾 Conversation enregistrée: Q='{question[:30]}...'")
    
    def get_last_n_conversations(self, n: int = 3) -> str:
        """
        Récupère les N dernières conversations au format texte.
        
        Args:
            n: Nombre de conversations à récupérer
            
        Returns:
            Historique formaté
        """
        if not self.history:
            return "Aucun historique disponible."
        
        # Prend les derniers messages (2 par conversation)
        recent = self.history[-(n*2):] if len(self.history) >= n*2 else self.history
        
        result = "📋 **HISTORIQUE RÉCENT:**\n"
        result += "-" * 40 + "\n"
        
        i = 0
        while i < len(recent):
            if i+1 < len(recent):
                q = recent[i]
                a = recent[i+1]
                
                if q['role'] == 'human' and a['role'] == 'ai':
                    result += f"👤 **Vous:** {q['content']}\n"
                    result += f"🤖 **DataBot:** {a['content']}\n"
                    result += f"⏰ {q['timestamp']}\n"
                    result += "-" * 30 + "\n"
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        
        return result
    
    def get_context_for_ai(self, max_length: int = 500) -> str:
        """
        Génère un contexte pour l'agent IA.
        
        Args:
            max_length: Longueur maximale du contexte
            
        Returns:
            Contexte formaté pour l'IA
        """
        if not self.history:
            return ""
        
        context = "CONTEXTE PRÉCÉDENT:\n"
        
        # Compte les caractères
        char_count = len(context)
        
        # Ajoute les conversations récentes (plus récentes d'abord)
        for i in range(len(self.history)-1, -1, -2):
            if i-1 >= 0:
                q = self.history[i-1] if self.history[i-1]['role'] == 'human' else None
                a = self.history[i] if self.history[i]['role'] == 'ai' else None
                
                if q and a:
                    conv_text = f"User: {q['content']}\nAssistant: {a['content']}\n---\n"
                    
                    if char_count + len(conv_text) > max_length:
                        break
                    
                    context = conv_text + context
                    char_count += len(conv_text)
        
        return context
    
    def get_stats(self) -> Dict[str, Any]:
        """Retourne des statistiques sur la mémoire"""
        human_msgs = sum(1 for msg in self.history if msg['role'] == 'human')
        ai_msgs = sum(1 for msg in self.history if msg['role'] == 'ai')
        
        return {
            "total_messages": len(self.history),
            "human_messages": human_msgs,
            "ai_messages": ai_msgs,
            "conversations": min(human_msgs, ai_msgs),
            "memory_usage_percent": (len(self.history) / self.max_messages) * 100
        }
    
    def clear(self) -> None:
        """Efface complètement l'historique"""
        self.history = []
        print("🗑️  Historique effacé")
    
    def save(self, filename: str = "memory_backup.json") -> bool:
        """
        Sauvegarde l'historique dans un fichier JSON.
        
        Args:
            filename: Nom du fichier de sauvegarde
            
        Returns:
            True si réussi, False sinon
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({
                    "history": self.history,
                    "max_messages": self.max_messages,
                    "saved_at": datetime.now().isoformat()
                }, f, ensure_ascii=False, indent=2)
            
            print(f"💾 Historique sauvegardé: {filename} ({len(self.history)} messages)")
            return True
            
        except Exception as e:
            print(f"❌ Erreur sauvegarde: {str(e)}")
            return False
    
    def load(self, filename: str = "memory_backup.json") -> bool:
        """
        Charge l'historique depuis un fichier JSON.
        
        Args:
            filename: Nom du fichier à charger
            
        Returns:
            True si réussi, False sinon
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.history = data.get("history", [])
            self.max_messages = data.get("max_messages", 20)
            
            print(f"📂 Historique chargé: {filename} ({len(self.history)} messages)")
            return True
            
        except FileNotFoundError:
            print(f"⚠️  Fichier non trouvé: {filename}")
            return False
        except json.JSONDecodeError:
            print(f"❌ Fichier JSON invalide: {filename}")
            return False
        except Exception as e:
            print(f"❌ Erreur chargement: {str(e)}")
            return False
    
    def search(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Recherche des messages contenant un mot-clé.
        
        Args:
            keyword: Mot-clé à rechercher
            
        Returns:
            Liste des messages correspondants
        """
        keyword_lower = keyword.lower()
        results = []
        
        for msg in self.history:
            if keyword_lower in msg['content'].lower():
                results.append(msg)
        
        return results
    
    def __str__(self) -> str:
        """Représentation textuelle de la mémoire"""
        stats = self.get_stats()
        return (f"MemoryManager: {stats['total_messages']} messages "
                f"({stats['human_messages']} humain, {stats['ai_messages']} AI)")

# Fonction utilitaire pour créer une instance
def create_memory_manager(max_messages: int = 20) -> MemoryManager:
    """
    Crée une instance de MemoryManager.
    
    Args:
        max_messages: Nombre maximum de messages
        
    Returns:
        Instance de MemoryManager
    """
    return MemoryManager(max_messages=max_messages)


# ==================== TEST INTÉGRÉ ====================
if __name__ == "__main__":
    print("🧪 TEST MEMORY MANAGER")
    print("=" * 50)
    
    # Création instance
    mm = create_memory_manager(max_messages=10)
    
    # Ajout de conversations
    test_conversations = [
        ("Bonjour DataBot", "Bonjour ! Je suis votre assistant commercial."),
        ("Quel est notre CA ?", "Le chiffre d'affaires est de 284,000 €."),
        ("Produit le plus vendu ?", "La souris gaming avec 342 unités."),
        ("Stock faible ?", "L'écran 4K a un stock faible: 32 unités.")
    ]
    
    for q, a in test_conversations:
        mm.add_conversation(q, a)
    
    # Affichage statistiques
    print("\n📊 STATISTIQUES:")
    stats = mm.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Affichage historique
    print("\n" + mm.get_last_n_conversations(2))
    
    # Test recherche
    print("\n🔍 RECHERCHE 'CA':")
    results = mm.search("CA")
    for msg in results:
        print(f"  [{msg['timestamp']}] {msg['role']}: {msg['content']}")
    
    # Test sauvegarde/chargement
    if mm.save("test_memory.json"):
        mm2 = create_memory_manager()
        if mm2.load("test_memory.json"):
            print(f"\n✅ Test sauvegarde/chargement réussi")
            print(f"   Messages chargés: {len(mm2.history)}")
    
    print("\n" + "=" * 50)
    print("✅ TEST TERMINÉ AVEC SUCCÈS")