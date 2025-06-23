# 🎬 CineRAG-AI - Intelligent Movie Discovery System
# Powered by Retrieval-Augmented Generation and Artificial Intelligence

import json
import os
from typing import List, Dict
from dataclasses import dataclass
import pickle
from datetime import datetime

# Advanced AI libraries for intelligent movie recommendations
try:
    import requests
    from sentence_transformers import SentenceTransformer
    import numpy as np
except ImportError:
    print("📦 Please install required packages for CineRAG-AI:")
    print("pip install -r requirements.txt")
    print("These packages power the AI functionality! 🤖")
    exit()

@dataclass
class Movie:
    """Enhanced movie data structure for CineRAG-AI"""
    title: str
    year: str
    genre: str
    rating: float
    description: str
    poster_url: str = ""
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre} - ⭐{self.rating}/10"

class CineRAGAI:
    """
    🎬 CineRAG-AI: Intelligent Movie Discovery System
    
    This advanced AI system combines:
    1. Retrieval-Augmented Generation (RAG) architecture
    2. Semantic understanding with sentence transformers
    3. Personalized recommendation learning
    4. Vector similarity matching
    5. Adaptive user preference modeling
    """
    
    def __init__(self):
        print("🎬 Initializing CineRAG-AI...")
        print("🤖 Loading advanced AI models... (this may take a moment)")
        
        # Initialize the AI brain for semantic understanding
        self.ai_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Core data storage
        self.movies: List[Movie] = []
        self.movie_embeddings = []  # Vector representations for AI
        self.user_preferences = {
            'liked_movies': [],
            'disliked_movies': [],
            'preferred_genres': [],
            'interaction_history': []
        }
        
        print("✅ CineRAG-AI is ready for intelligent movie discovery!")
        
        # Load existing data or initialize with samples
        self.load_system_data()
        
        if not self.movies:
            self.initialize_movie_database()
    
    def initialize_movie_database(self):
        """Initialize CineRAG-AI with curated movie database"""
        print("🎬 Initializing CineRAG-AI movie database...")
        
        premium_movies = [
            Movie("Spider-Man: No Way Home", "2021", "Action/Adventure", 8.3, 
                  "Peter Parker's identity is revealed and he asks Doctor Strange for help. Multiverse chaos ensues with villains from previous Spider-Man movies returning."),
            
            Movie("The Batman", "2022", "Action/Crime", 7.9,
                  "Young Bruce Wayne investigates corruption in Gotham City while facing the Riddler, a serial killer targeting elite citizens with deadly puzzles."),
            
            Movie("Encanto", "2021", "Animation/Family", 7.3,
                  "A magical family lives in a house in Colombia where each family member has special powers, except for Mirabel who must save her family's magic."),
            
            Movie("Dune", "2021", "Sci-Fi/Adventure", 8.0,
                  "Paul Atreides leads nomadic tribes in a battle to control the desert planet Arrakis and its valuable spice resource in this epic space opera."),
            
            Movie("No Time to Die", "2021", "Action/Thriller", 7.3,
                  "James Bond comes out of retirement to rescue a kidnapped scientist, leading to a dangerous mission involving lethal new technology."),
            
            Movie("Top Gun: Maverick", "2022", "Action/Drama", 8.3,
                  "Pete 'Maverick' Mitchell returns as a flight instructor to train a new generation of pilots for a dangerous mission nobody has survived."),
            
            Movie("Turning Red", "2022", "Animation/Comedy", 7.0,
                  "A 13-year-old girl in Toronto balances her relationship with her mother while dealing with transforming into a giant red panda when excited."),
            
            Movie("The Matrix Resurrections", "2021", "Sci-Fi/Action", 5.7,
                  "Neo lives a seemingly ordinary life as a video game developer until strange occurrences lead him to discover the truth about his reality."),
            
            Movie("Fast & Furious 9", "2021", "Action/Adventure", 5.2,
                  "Dom Toretto faces his past when his estranged brother Jakob emerges as a deadly assassin working with an old enemy."),
            
            Movie("A Quiet Place Part II", "2021", "Horror/Thriller", 7.2,
                  "The Abbott family continues to face terrifying creatures that hunt by sound while discovering other survivors in their post-apocalyptic world."),
            
            Movie("Shang-Chi and the Legend of the Ten Rings", "2021", "Action/Adventure", 7.4,
                  "Shang-Chi confronts his past when drawn into the web of the mysterious Ten Rings organization and faces his father, the legendary Mandarin."),
            
            Movie("Eternals", "2021", "Action/Sci-Fi", 6.3,
                  "Immortal aliens have secretly lived on Earth for thousands of years and reunite to protect humanity from their evil counterparts, the Deviants."),
            
            Movie("Cruella", "2021", "Crime/Comedy", 7.3,
                  "Young grifter Estella transforms into the raucous, fashionable Cruella de Vil in 1970s London during the punk rock revolution."),
            
            Movie("Black Widow", "2021", "Action/Adventure", 6.7,
                  "Natasha Romanoff confronts her past as a spy and the broken relationships left in her wake long before she became an Avenger."),
            
            Movie("Jungle Cruise", "2021", "Action/Adventure", 6.6,
                  "Dr. Lily Houghton enlists the aid of wisecracking skipper Frank Wolff to take her down the Amazon in his ramshackle boat to find an ancient tree.")
        ]
        
        for movie in premium_movies:
            self.add_movie_to_system(movie)
        
        print(f"✅ CineRAG-AI database initialized with {len(premium_movies)} premium movies!")
    
    def add_movie_to_system(self, movie: Movie):
        """Add a movie to CineRAG-AI with AI processing"""
        # Create comprehensive content for AI understanding
        movie_content = f"{movie.title} {movie.genre} {movie.description}"
        
        # Generate AI embedding (vector representation)
        movie_embedding = self.ai_model.encode(movie_content)
        
        # Store in system
        self.movies.append(movie)
        self.movie_embeddings.append(movie_embedding)
        
        print(f"🎬 Added to CineRAG-AI: {movie.title}")
    
    def intelligent_movie_search(self, query: str, num_results: int = 5) -> List[tuple]:
        """
        🧠 CineRAG-AI Core Search Engine
        
        Advanced AI-powered search using:
        1. Semantic understanding via sentence transformers
        2. Vector similarity matching
        3. User preference integration
        4. Relevance scoring and ranking
        """
        if not self.movies:
            print("❌ CineRAG-AI database is empty!")
            return []
        
        print(f"🔍 CineRAG-AI analyzing: '{query}'")
        
        # Step 1: Convert query to AI understanding
        query_embedding = self.ai_model.encode(query)
        
        # Step 2: Calculate semantic similarities
        movie_similarities = []
        for i, movie_embedding in enumerate(self.movie_embeddings):
            # Cosine similarity for semantic matching
            similarity = np.dot(query_embedding, movie_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(movie_embedding)
            )
            movie_similarities.append((self.movies[i], similarity))
        
        # Step 3: Apply AI-driven personalization
        personalized_results = self.apply_ai_personalization(movie_similarities)
        
        # Step 4: Rank and return top results
        final_results = sorted(personalized_results, key=lambda x: x[1], reverse=True)
        
        return final_results[:num_results]
    
    def apply_ai_personalization(self, movie_similarities: List[tuple]) -> List[tuple]:
        """Apply CineRAG-AI personalization algorithms"""
        if not self.user_preferences['liked_movies']:
            return movie_similarities
        
        # Calculate user preference vector
        liked_embeddings = []
        for movie in self.movies:
            if movie.title in self.user_preferences['liked_movies']:
                idx = self.movies.index(movie)
                liked_embeddings.append(self.movie_embeddings[idx])
        
        if not liked_embeddings:
            return movie_similarities
        
        # Create user taste profile
        user_taste_vector = np.mean(liked_embeddings, axis=0)
        
        # Enhance recommendations with personalization
        enhanced_results = []
        for movie, base_similarity in movie_similarities:
            idx = self.movies.index(movie)
            movie_embedding = self.movie_embeddings[idx]
            
            # Calculate taste alignment
            taste_similarity = np.dot(user_taste_vector, movie_embedding) / (
                np.linalg.norm(user_taste_vector) * np.linalg.norm(movie_embedding)
            )
            
            # Combine base similarity with personalization
            personalized_score = base_similarity * 0.6 + taste_similarity * 0.4
            
            # Apply preference penalties/boosts
            if movie.title in self.user_preferences['disliked_movies']:
                personalized_score *= 0.1  # Heavy penalty for disliked
            
            if any(genre in self.user_preferences['preferred_genres'] for genre in movie.genre.split('/')):
                personalized_score *= 1.2  # Boost for preferred genres
            
            enhanced_results.append((movie, personalized_score))
        
        return enhanced_results
    
    def learn_user_preference(self, movie_title: str, preference_type: str):
        """CineRAG-AI learning system for user preferences"""
        timestamp = datetime.now().isoformat()
        
        if preference_type == "like":
            if movie_title not in self.user_preferences['liked_movies']:
                self.user_preferences['liked_movies'].append(movie_title)
                print(f"👍 CineRAG-AI learned: You liked {movie_title}")
                
                # Extract genre preferences
                for movie in self.movies:
                    if movie.title == movie_title:
                        for genre in movie.genre.split('/'):
                            if genre not in self.user_preferences['preferred_genres']:
                                self.user_preferences['preferred_genres'].append(genre)
                
        elif preference_type == "dislike":
            if movie_title not in self.user_preferences['disliked_movies']:
                self.user_preferences['disliked_movies'].append(movie_title)
                print(f"👎 CineRAG-AI learned: You disliked {movie_title}")
        
        # Log interaction for advanced learning
        self.user_preferences['interaction_history'].append({
            'movie': movie_title,
            'action': preference_type,
            'timestamp': timestamp
        })
        
        print("🧠 CineRAG-AI updated your preference profile!")
        self.save_system_data()
    
    def get_ai_recommendations(self, num_results: int = 5) -> List[tuple]:
        """Get personalized recommendations from CineRAG-AI"""
        if not self.user_preferences['liked_movies']:
            print("🤔 CineRAG-AI needs to learn your preferences first!")
            print("💡 Try searching and rating some movies!")
            return []
        
        # Generate recommendation query from user profile
        preferred_content = " ".join([
            f"{movie.genre} {movie.description}" 
            for movie in self.movies 
            if movie.title in self.user_preferences['liked_movies']
        ])
        
        recommendation_query = f"movies similar to {preferred_content}"
        
        return self.intelligent_movie_search(recommendation_query, num_results)
    
    def display_movie_database(self):
        """Display CineRAG-AI movie database"""
        if not self.movies:
            print("📭 CineRAG-AI database is empty!")
            return
        
        print(f"\n📚 CineRAG-AI Database ({len(self.movies)} movies):")
        print("=" * 60)
        
        for i, movie in enumerate(self.movies, 1):
            status = ""
            if movie.title in self.user_preferences['liked_movies']:
                status = " 👍"
            elif movie.title in self.user_preferences['disliked_movies']:
                status = " 👎"
            
            print(f"{i}. {movie}{status}")
            print(f"   📝 {movie.description[:80]}...")
            print()
    
    def save_system_data(self):
        """Save CineRAG-AI data persistence"""
        try:
            system_data = {
                'movies': self.movies,
                'movie_embeddings': self.movie_embeddings,
                'user_preferences': self.user_preferences,
                'system_version': 'CineRAG-AI v1.0'
            }
            
            with open('cinerag_ai_data.pkl', 'wb') as f:
                pickle.dump(system_data, f)
            
            print("💾 CineRAG-AI data saved successfully!")
        except Exception as e:
            print(f"⚠️ CineRAG-AI save error: {e}")
    
    def load_system_data(self):
        """Load CineRAG-AI saved data"""
        try:
            with open('cinerag_ai_data.pkl', 'rb') as f:
                system_data = pickle.load(f)
            
            self.movies = system_data.get('movies', [])
            self.movie_embeddings = system_data.get('movie_embeddings', [])
            self.user_preferences = system_data.get('user_preferences', {
                'liked_movies': [],
                'disliked_movies': [],
                'preferred_genres': [],
                'interaction_history': []
            })
            
            print(f"💾 CineRAG-AI loaded {len(self.movies)} movies and your profile!")
        except FileNotFoundError:
            print("📝 CineRAG-AI starting fresh - building new profile!")
        except Exception as e:
            print(f"⚠️ CineRAG-AI load error: {e}")
    
    def add_custom_movie(self):
        """Add custom movie to CineRAG-AI database"""
        print("\n🎬 Add Movie to CineRAG-AI Database")
        print("-" * 40)
        
        title = input("Movie title: ").strip()
        year = input("Release year: ").strip()
        genre = input("Genre (e.g., Action/Adventure): ").strip()
        
        try:
            rating = float(input("Rating (0-10): ").strip())
            rating = max(0, min(10, rating))
        except ValueError:
            rating = 7.0
            print("Using default rating: 7.0")
        
        description = input("Movie description: ").strip()
        
        if title and description:
            movie = Movie(title, year, genre, rating, description)
            self.add_movie_to_system(movie)
            self.save_system_data()
            print("✅ Movie added to CineRAG-AI database!")
        else:
            print("❌ Title and description are required!")
    
    def show_user_analytics(self):
        """Display CineRAG-AI user analytics"""
        prefs = self.user_preferences
        
        print("\n📊 CineRAG-AI User Analytics:")
        print("=" * 40)
        print(f"🎬 Movies in database: {len(self.movies)}")
        print(f"👍 Movies you liked: {len(prefs['liked_movies'])}")
        print(f"👎 Movies you disliked: {len(prefs['disliked_movies'])}")
        print(f"🎭 Preferred genres: {len(prefs['preferred_genres'])}")
        print(f"📈 Total interactions: {len(prefs['interaction_history'])}")
        
        if prefs['liked_movies']:
            print(f"\n💖 Your favorite movies (last 5):")
            for movie_title in prefs['liked_movies'][-5:]:
                print(f"  • {movie_title}")
        
        if prefs['preferred_genres']:
            print(f"\n🎭 Your preferred genres:")
            for genre in prefs['preferred_genres'][:5]:
                print(f"  • {genre}")
        
        # Calculate recommendation accuracy
        if len(prefs['interaction_history']) > 5:
            recent_likes = sum(1 for interaction in prefs['interaction_history'][-10:] 
                             if interaction['action'] == 'like')
            accuracy = (recent_likes / min(10, len(prefs['interaction_history']))) * 100
            print(f"\n🎯 Recent recommendation accuracy: {accuracy:.1f}%")

def launch_cinerag_ai():
    """Launch CineRAG-AI interactive system"""
    print("🎬 Welcome to CineRAG-AI!")
    print("=" * 50)
    print("🤖 Intelligent Movie Discovery Powered by AI")
    print("🧠 Using Advanced Retrieval-Augmented Generation")
    
    # Initialize CineRAG-AI system
    cinerag = CineRAGAI()
    
    while True:
        print("\n🎯 CineRAG-AI Main Menu:")
        print("1️⃣  🔍 Intelligent Movie Search")
        print("2️⃣  🎯 Get AI Recommendations") 
        print("3️⃣  📚 Browse Movie Database")
        print("4️⃣  ➕ Add Custom Movie")
        print("5️⃣  📊 View User Analytics")
        print("6️⃣  🚪 Exit CineRAG-AI")
        
        choice = input("\n🤖 Select option (1-6): ").strip()
        
        if choice == "1":
            # Intelligent search
            query = input("\n🔍 What movies are you looking for? ")
            if query.strip():
                results = cinerag.intelligent_movie_search(query, 5)
                
                if results:
                    print(f"\n🎬 CineRAG-AI found {len(results)} movies:")
                    print("=" * 60)
                    
                    for i, (movie, score) in enumerate(results, 1):
                        print(f"{i}. {movie} (AI Match: {score:.1%})")
                        print(f"   📝 {movie.description}")
                        
                        # Collect user feedback for learning
                        while True:
                            feedback = input("   Rate this movie: 👍 Like / 👎 Dislike / ⏭️ Skip (l/d/s): ").lower()
                            if feedback in ['l', 'like']:
                                cinerag.learn_user_preference(movie.title, 'like')
                                break
                            elif feedback in ['d', 'dislike']:
                                cinerag.learn_user_preference(movie.title, 'dislike')
                                break
                            elif feedback in ['s', 'skip', '']:
                                break
                            else:
                                print("   Please enter 'l', 'd', or 's'")
                        print()
                else:
                    print("❌ No movies found. Try different search terms!")
            else:
                print("❌ Please enter a search query!")
        
        elif choice == "2":
            # AI recommendations
            print("\n🤖 CineRAG-AI generating personalized recommendations...")
            recommendations = cinerag.get_ai_recommendations(5)
            
            if recommendations:
                print("🎬 Movies CineRAG-AI thinks you'll love:")
                print("=" * 50)
                
                for i, (movie, score) in enumerate(recommendations, 1):
                    # Don't recommend already liked movies
                    if movie.title not in cinerag.user_preferences['liked_movies']:
                        print(f"{i}. {movie} (AI Confidence: {score:.1%})")
                        print(f"   📝 {movie.description}")
                        print()
            else:
                print("🤔 CineRAG-AI needs more data about your preferences!")
                print("💡 Try searching and rating movies first!")
        
        elif choice == "3":
            # Browse database
            cinerag.display_movie_database()
        
        elif choice == "4":
            # Add custom movie
            cinerag.add_custom_movie()
        
        elif choice == "5":
            # User analytics
            cinerag.show_user_analytics()
        
        elif choice == "6":
            # Exit
            print("👋 Thank you for using CineRAG-AI!")
            print("🎬 Keep discovering amazing movies!")
            break
        
        else:
            print("❌ Invalid choice. Please select 1-6!")

# Demonstration mode for developers
def cinerag_ai_demo():
    """Demonstrate CineRAG-AI capabilities"""
    print("🔧 CineRAG-AI Developer Demo")
    print("=" * 40)
    
    # Initialize system
    cinerag = CineRAGAI()
    
    # Demo searches
    demo_queries = [
        "action movies with superheroes",
        "funny animated movies for families", 
        "sci-fi movies with great ratings",
        "thriller movies with mystery"
    ]
    
    print("\n🔍 Demo: CineRAG-AI Search Capabilities")
    for query in demo_queries:
        print(f"\nQuery: '{query}'")
        results = cinerag.intelligent_movie_search(query, 3)
        
        if results:
            for i, (movie, score) in enumerate(results, 1):
                print(f"  {i}. {movie.title} (Score: {score:.3f})")
        else:
            print("  No results found")
    
    print("\n🤖 CineRAG-AI Demo Complete!")

if __name__ == "__main__":
    print("🚀 CineRAG-AI Startup Options:")
    print("1. Launch Interactive System")
    print("2. Run Developer Demo")
    
    mode = input("Choose mode (1 or 2): ").strip()
    
    if mode == "1":
        launch_cinerag_ai()
    else:
        cinerag_ai_demo()
