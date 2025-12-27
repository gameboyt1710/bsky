#!/usr/bin/env python3
"""
Test script for On This Day Bot
Tests Wikipedia API functionality without requiring Bluesky credentials.
"""

import sys
from on_this_day_bot import WikipediaOnThisDay, format_event, format_birth, format_death

def test_wikipedia_api():
    """Test Wikipedia API fetching."""
    print("Testing Wikipedia API...")
    wiki = WikipediaOnThisDay()
    
    # Test events
    print("\n1. Fetching events...")
    events = wiki.get_events()
    if events:
        print(f"   ✓ Successfully fetched {len(events)} events")
        print(f"   Example: {events[0].get('text', 'N/A')[:80]}...")
    else:
        print("   ✗ Failed to fetch events")
        return False
    
    # Test births
    print("\n2. Fetching births...")
    births = wiki.get_births()
    if births:
        print(f"   ✓ Successfully fetched {len(births)} births")
        print(f"   Example: {births[0].get('text', 'N/A')[:80]}...")
    else:
        print("   ✗ Failed to fetch births")
        return False
    
    # Test deaths
    print("\n3. Fetching deaths...")
    deaths = wiki.get_deaths()
    if deaths:
        print(f"   ✓ Successfully fetched {len(deaths)} deaths")
        print(f"   Example: {deaths[0].get('text', 'N/A')[:80]}...")
    else:
        print("   ✗ Failed to fetch deaths")
        return False
    
    return True

def test_formatting():
    """Test fact formatting."""
    print("\n\nTesting formatting functions...")
    
    # Test event formatting
    print("\n1. Testing event formatting...")
    test_event = {
        'year': 1969,
        'text': 'Apollo 11 astronauts Neil Armstrong and Buzz Aldrin became the first humans to walk on the Moon.'
    }
    formatted = format_event(test_event)
    print(f"   Formatted event:\n   {formatted.replace('\n', '\n   ')}")
    
    # Test birth formatting
    print("\n2. Testing birth formatting...")
    test_birth = {
        'year': 1867,
        'text': 'Marie Curie, Polish-French physicist and chemist.'
    }
    formatted = format_birth(test_birth)
    print(f"   Formatted birth:\n   {formatted.replace('\n', '\n   ')}")
    
    # Test death formatting
    print("\n3. Testing death formatting...")
    test_death = {
        'year': 1965,
        'text': 'Winston Churchill, British Prime Minister.'
    }
    formatted = format_death(test_death)
    print(f"   Formatted death:\n   {formatted.replace('\n', '\n   ')}")
    
    return True

def test_full_workflow():
    """Test the full workflow of selecting a random fact."""
    print("\n\nTesting full workflow...")
    from on_this_day_bot import select_random_fact
    
    print("\nSelecting random fact...")
    fact = select_random_fact()
    
    if fact:
        print(f"✓ Successfully selected fact:\n\n{fact}")
        print(f"\nLength: {len(fact)} characters (max 300 for Bluesky)")
        if len(fact) > 300:
            print(f"⚠ Warning: Fact is too long and will be truncated")
        return True
    else:
        print("✗ Failed to select fact")
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("On This Day Bot - Test Suite")
    print("=" * 60)
    
    tests_passed = 0
    tests_total = 3
    
    # Test 1: Wikipedia API
    if test_wikipedia_api():
        tests_passed += 1
        print("\n✓ Wikipedia API test passed")
    else:
        print("\n✗ Wikipedia API test failed")
    
    # Test 2: Formatting
    if test_formatting():
        tests_passed += 1
        print("\n✓ Formatting test passed")
    else:
        print("\n✗ Formatting test failed")
    
    # Test 3: Full workflow
    if test_full_workflow():
        tests_passed += 1
        print("\n✓ Full workflow test passed")
    else:
        print("\n✗ Full workflow test failed")
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Test Results: {tests_passed}/{tests_total} tests passed")
    print("=" * 60)
    
    if tests_passed == tests_total:
        print("\n✓ All tests passed! The bot is ready to use.")
        print("\nNext steps:")
        print("1. Copy .env.example to .env")
        print("2. Add your Bluesky credentials to .env")
        print("3. Run: python3 on_this_day_bot.py")
        return 0
    else:
        print("\n✗ Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
