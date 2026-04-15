"""Count words in a list of 50 app reviews and print summary stats."""


reviews = [
    "This app helps me track my tasks quickly and I use it every morning before work.",
    "The design is clean and simple but I wish the notifications were easier to customize.",
    "I like the dark mode and the calendar sync because it keeps my week organized.",
    "Sometimes the app freezes when I open it after an update and I have to restart.",
    "Great onboarding flow and very clear labels across each screen of the interface.",
    "The search feature works well for recent notes but struggles with older archived items.",
    "I use this during classes and it helps me collect ideas without losing focus.",
    "The app is useful overall, though loading feels slow when my internet is unstable.",
    "I appreciate the reminders because they help me remember deadlines and group meetings.",
    "I wish there were more color themes for accessibility and personal preferences.",
    "Navigation is intuitive and I found the core features without needing any tutorial.",
    "The recent update improved performance and now screens open much faster than before.",
    "I had trouble resetting my password but customer support replied within one day.",
    "The app is good for planning, but collaboration tools still feel limited to me.",
    "I enjoy the progress charts because they make weekly goals easier to reflect on.",
    "Voice input is surprisingly accurate and saves me time while commuting to campus.",
    "Please add offline mode so I can still edit content during poor connectivity.",
    "The widget feature is helpful and lets me see tasks without opening the app.",
    "Sometimes I accidentally delete items because the swipe gesture feels too sensitive.",
    "This app made team coordination easier and reduced confusion about shared deadlines.",
    "I like the minimal interface and the icons are readable even on small screens.",
    "The login process is smooth and I have not had any major account issues.",
    "I would love better export options for reports because I share data with classmates.",
    "Push notifications can be noisy, but turning them off is straightforward and quick.",
    "The tutorial videos were short and practical, which made setup less intimidating.",
    "I noticed bugs in the tagging system where labels sometimes duplicate unexpectedly.",
    "The app helps me plan research sessions and keep participant notes in one place.",
    "I enjoy the weekly summary email because it gives me a clear productivity snapshot.",
    "Please improve contrast on buttons because some text is hard to read in sunlight.",
    "Overall this is one of the few tools I still use after the first month.",
    "Collaboration comments are useful and keep feedback attached to each relevant task.",
    "I had a crash yesterday when attaching a file larger than ten megabytes.",
    "The app syncs quickly across devices and that makes switching contexts much easier.",
    "I like the template library because it saves me from repeating routine setup steps.",
    "The pricing is reasonable for students, especially with the current education discount.",
    "I wish there was a way to pin favorite projects at the top of the list.",
    "The reporting dashboard looks polished and communicates trends in a very readable way.",
    "Sometimes scrolling stutters on older phones, but behavior is smoother on my tablet.",
    "I like how easy it is to duplicate recurring tasks for weekly planning.",
    "Customer support was polite and gave useful troubleshooting tips that solved my issue.",
    "The app feels reliable and I trust it for storing notes from interviews.",
    "I wish there were keyboard shortcuts for faster navigation on desktop versions.",
    "The new sharing permissions are excellent and help protect sensitive project information.",
    "There is a learning curve at first, but the help center articles are clear.",
    "I appreciate that updates are frequent and usually include meaningful quality improvements.",
    "The app is pretty good, though I still want deeper integration with calendars.",
    "I use it for personal goals and team work, and it handles both well.",
    "Exported files sometimes lose formatting, which creates extra cleanup work for me.",
    "The search filters are powerful and help me find exactly what I need quickly.",
    "Overall I recommend this app because it balances simplicity with useful functionality.",
]

#This functions is used to count the numder of the words in the string 
def count_words(text):
    """Return the number of words in a string."""
    return len(text.split())

#this is to check that the number is exactly 50 
if len(reviews) != 50:
    raise ValueError("Expected exactly 50 reviews in the list.")
# this is to pring the review, words and preview 
print(f"{'Review #':<10} {'Words':<6} {'Preview'}")
print("-" * 72)
#This counts the words in the review 
word_counts = []
for i, review in enumerate(reviews, start=1):
    words = count_words(review)
    word_counts.append(words)
    preview = review[:60] + "..." if len(review) > 60 else review
    print(f"{i:<10} {words:<6} {preview}")

print()
print("Summary")
print("-" * 72)
print(f"Total reviews : {len(reviews)}")
print(f"Shortest      : {min(word_counts)} words")
print(f"Longest       : {max(word_counts)} words")
print(f"Average       : {sum(word_counts) / len(word_counts):.1f} words")
