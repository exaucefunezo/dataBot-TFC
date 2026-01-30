# modules/chart_generator.py - VERSION CORRIGÉE
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

class ChartGenerator:
    """Générateur de graphiques pour DataBot"""
    
    @staticmethod
    def generate_sales_bar(data, x_col='product', y_col='total_quantity', title="Ventes par Produit"):
        """Génère un graphique à barres des ventes"""
        try:
            fig = px.bar(
                data, 
                x=x_col, 
                y=y_col, 
                title=title,
                color=x_col,
                text=y_col
            )
            fig.update_layout(
                xaxis_title="Produit",
                yaxis_title="Quantité Vendue",
                showlegend=False
            )
            return fig
        except Exception as e:
            print(f"❌ Erreur génération graphique barres: {e}")
            return None
    
    @staticmethod
    def generate_revenue_pie(data, value_col='total_revenue', name_col='product', title="Répartition du CA"):
        """Génère un graphique camembert des revenus"""
        try:
            fig = px.pie(
                data, 
                values=value_col, 
                names=name_col, 
                title=title,
                hole=0.3  # Donut chart
            )
            return fig
        except Exception as e:
            print(f"❌ Erreur génération graphique pie: {e}")
            return None
    
    @staticmethod
    def generate_trend_line(data, x_col='date', y_col='quantity', title="Tendance des Ventes"):
        """Génère un graphique de tendance linéaire"""
        try:
            fig = px.line(
                data, 
                x=x_col, 
                y=y_col, 
                title=title,
                markers=True
            )
            fig.update_layout(
                xaxis_title="Date",
                yaxis_title="Quantité"
            )
            return fig
        except Exception as e:
            print(f"❌ Erreur génération graphique ligne: {e}")
            return None
    
    @staticmethod
    def save_chart(fig, filename="graphique.png"):
        """Sauvegarde un graphique en fichier"""
        try:
            fig.write_image(filename)
            print(f"✅ Graphique sauvegardé: {filename}")
            return True
        except Exception as e:
            print(f"❌ Erreur sauvegarde graphique: {e}")
            return False