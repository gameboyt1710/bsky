#!/usr/bin/env python3
"""
On This Day Bluesky Bot
Fetches "On This Day" facts from Wikipedia and posts them to Bluesky.
"""

import os
import sys
import random
import requests
from datetime import datetime
from typing import List, Dict, Optional
from dotenv import load_dotenv
from atproto import Client

# Load environment variables
load_dotenv()


class WikipediaOnThisDay:
    """Fetches 'On This Day' facts from Wikipedia API."""
    
    BASE_URL = "https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'OnThisDayBot/1.0 (Bluesky Bot; Educational Purpose)'
        })
    
    def get_events(self, month: Optional[int] = None, day: Optional[int] = None) -> List[Dict]:
        """
        Fetch events that happened on this day in history.
        
        Args:
            month: Month (1-12). Defaults to current month.
            day: Day (1-31). Defaults to current day.
            
        Returns:
            List of event dictionaries.
        """
        now = datetime.now()
        month = month or now.month
        day = day or now.day
        
        url = f"{self.BASE_URL}/events/{month}/{day}"
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get('events', [])
        except requests.RequestException as e:
            print(f"Error fetching Wikipedia data: {e}")
            return []
    
    def get_births(self, month: Optional[int] = None, day: Optional[int] = None) -> List[Dict]:
        """
        Fetch births that happened on this day in history.
        
        Args:
            month: Month (1-12). Defaults to current month.
            day: Day (1-31). Defaults to current day.
            
        Returns:
            List of birth dictionaries.
        """
        now = datetime.now()
        month = month or now.month
        day = day or now.day
        
        url = f"{self.BASE_URL}/births/{month}/{day}"
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get('births', [])
        except requests.RequestException as e:
            print(f"Error fetching Wikipedia data: {e}")
            return []
    
    def get_deaths(self, month: Optional[int] = None, day: Optional[int] = None) -> List[Dict]:
        """
        Fetch deaths that happened on this day in history.
        
        Args:
            month: Month (1-12). Defaults to current month.
            day: Day (1-31). Defaults to current day.
            
        Returns:
            List of death dictionaries.
        """
        now = datetime.now()
        month = month or now.month
        day = day or now.day
        
        url = f"{self.BASE_URL}/deaths/{month}/{day}"
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get('deaths', [])
        except requests.RequestException as e:
            print(f"Error fetching Wikipedia data: {e}")
            return []


class BlueskyBot:
    """Bluesky bot for posting content."""
    
    def __init__(self, handle: str, password: str):
        """
        Initialize Bluesky bot.
        
        Args:
            handle: Bluesky handle (e.g., username.bsky.social)
            password: Bluesky app password
        """
        self.handle = handle
        self.password = password
        self.client = Client()
    
    def login(self) -> bool:
        """
        Login to Bluesky.
        
        Returns:
            True if login successful, False otherwise.
        """
        try:
            self.client.login(self.handle, self.password)
            print(f"Successfully logged in as {self.handle}")
            return True
        except Exception as e:
            print(f"Error logging in: {e}")
            return False
    
    def post(self, text: str) -> bool:
        """
        Post text to Bluesky.
        
        Args:
            text: Text content to post (max 300 characters).
            
        Returns:
            True if post successful, False otherwise.
        """
        if len(text) > 300:
            print(f"Warning: Text is {len(text)} characters. Truncating to 300.")
            text = text[:297] + "..."
        
        try:
            self.client.send_post(text=text)
            print(f"Successfully posted: {text[:50]}...")
            return True
        except Exception as e:
            print(f"Error posting to Bluesky: {e}")
            return False


def format_event(event: Dict) -> str:
    """
    Format a Wikipedia event for posting.
    
    Args:
        event: Event dictionary from Wikipedia API.
        
    Returns:
        Formatted string for posting.
    """
    year = event.get('year', 'Unknown')
    text = event.get('text', '')
    
    # Remove HTML tags if any
    import re
    text = re.sub('<[^<]+?>', '', text)
    
    return f"📅 On This Day in {year}:\n\n{text}"


def format_birth(birth: Dict) -> str:
    """
    Format a Wikipedia birth for posting.
    
    Args:
        birth: Birth dictionary from Wikipedia API.
        
    Returns:
        Formatted string for posting.
    """
    year = birth.get('year', 'Unknown')
    text = birth.get('text', '')
    
    # Remove HTML tags if any
    import re
    text = re.sub('<[^<]+?>', '', text)
    
    return f"🎂 Born On This Day in {year}:\n\n{text}"


def format_death(death: Dict) -> str:
    """
    Format a Wikipedia death for posting.
    
    Args:
        death: Death dictionary from Wikipedia API.
        
    Returns:
        Formatted string for posting.
    """
    year = death.get('year', 'Unknown')
    text = death.get('text', '')
    
    # Remove HTML tags if any
    import re
    text = re.sub('<[^<]+?>', '', text)
    
    return f"🕊️ Died On This Day in {year}:\n\n{text}"


def get_sample_facts() -> List[tuple]:
    """
    Get sample facts for demo/testing purposes.
    
    Returns:
        List of (fact_type, fact_data) tuples.
    """
    sample_events = [
        {'year': 1969, 'text': 'Apollo 11 astronauts Neil Armstrong and Buzz Aldrin became the first humans to walk on the Moon.'},
        {'year': 1989, 'text': 'The Berlin Wall fell, marking the end of the Cold War era and German division.'},
        {'year': 1945, 'text': 'World War II ended in Europe with Germany\'s unconditional surrender.'},
    ]
    
    sample_births = [
        {'year': 1867, 'text': 'Marie Curie, Polish-French physicist and chemist who conducted pioneering research on radioactivity.'},
        {'year': 1564, 'text': 'William Shakespeare, English playwright and poet, widely regarded as the greatest writer in the English language.'},
        {'year': 1879, 'text': 'Albert Einstein, German-born theoretical physicist who developed the theory of relativity.'},
    ]
    
    sample_deaths = [
        {'year': 1965, 'text': 'Winston Churchill, British Prime Minister during World War II and Nobel Prize winner in Literature.'},
        {'year': 2016, 'text': 'Muhammad Ali, American professional boxer and activist, widely regarded as one of the greatest athletes of all time.'},
        {'year': 1980, 'text': 'John Lennon, English singer, songwriter, and peace activist, co-founder of The Beatles.'},
    ]
    
    facts = []
    for event in sample_events:
        facts.append(('event', event))
    for birth in sample_births:
        facts.append(('birth', birth))
    for death in sample_deaths:
        facts.append(('death', death))
    
    return facts


def select_random_fact(use_sample: bool = False) -> Optional[str]:
    """
    Select a random fact from Wikipedia's "On This Day" data.
    
    Args:
        use_sample: If True, use sample data instead of fetching from Wikipedia.
    
    Returns:
        Formatted fact string or None if no facts available.
    """
    if use_sample:
        print("Using sample data (demo mode)")
        all_facts = get_sample_facts()
    else:
        wiki = WikipediaOnThisDay()
        
        # Fetch all types of facts
        events = wiki.get_events()
        births = wiki.get_births()
        deaths = wiki.get_deaths()
        
        # Combine all facts with their formatters
        all_facts = []
        
        for event in events:
            all_facts.append(('event', event))
        
        for birth in births:
            all_facts.append(('birth', birth))
        
        for death in deaths:
            all_facts.append(('death', death))
    
    if not all_facts:
        print("No facts available")
        return None
    
    # Select random fact
    fact_type, fact_data = random.choice(all_facts)
    
    # Format based on type
    if fact_type == 'event':
        return format_event(fact_data)
    elif fact_type == 'birth':
        return format_birth(fact_data)
    elif fact_type == 'death':
        return format_death(fact_data)
    
    return None


def main():
    """Main function to run the bot."""
    # Check for demo mode
    demo_mode = '--demo' in sys.argv or '--test' in sys.argv
    
    if demo_mode:
        print("Running in DEMO MODE - will not post to Bluesky")
        print("=" * 60)
        
        # Get a random fact using sample data
        print("\nFetching sample 'On This Day' fact...")
        fact = select_random_fact(use_sample=True)
        
        if not fact:
            print("Failed to generate fact")
            sys.exit(1)
        
        print(f"\nGenerated fact:\n")
        print("-" * 60)
        print(fact)
        print("-" * 60)
        print(f"\nLength: {len(fact)} characters (max 300 for Bluesky)")
        
        if len(fact) > 300:
            print(f"\n⚠ Warning: This fact would be truncated to 300 characters")
            print(f"\nTruncated version:")
            print("-" * 60)
            print(fact[:297] + "...")
            print("-" * 60)
        
        print("\n✓ Demo completed successfully!")
        print("\nTo post to Bluesky for real, run without --demo flag")
        sys.exit(0)
    
    # Get credentials from environment
    handle = os.getenv('BLUESKY_HANDLE')
    password = os.getenv('BLUESKY_PASSWORD')
    
    if not handle or not password:
        print("Error: BLUESKY_HANDLE and BLUESKY_PASSWORD must be set in .env file")
        print("Please copy .env.example to .env and fill in your credentials")
        print("\nTip: Run with --demo flag to test without credentials")
        sys.exit(1)
    
    # Get a random fact
    print("Fetching 'On This Day' fact from Wikipedia...")
    fact = select_random_fact(use_sample=False)
    
    if not fact:
        print("Failed to fetch fact from Wikipedia")
        print("Falling back to sample data...")
        fact = select_random_fact(use_sample=True)
        
        if not fact:
            print("Failed to generate fact")
            sys.exit(1)
    
    print(f"\nFact to post:\n{fact}\n")
    
    # Initialize and login to Bluesky
    bot = BlueskyBot(handle, password)
    
    if not bot.login():
        print("Failed to login to Bluesky")
        sys.exit(1)
    
    # Post the fact
    if bot.post(fact):
        print("Successfully posted to Bluesky!")
        sys.exit(0)
    else:
        print("Failed to post to Bluesky")
        sys.exit(1)


if __name__ == "__main__":
    main()
