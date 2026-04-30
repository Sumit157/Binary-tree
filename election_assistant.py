#!/usr/bin/env python3
"""Interactive election process assistant (U.S.-focused baseline)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ElectionStep:
    title: str
    why_it_matters: str
    action: str


TIMELINE = [
    ("6-12 months before Election Day", "Check/update voter registration and address."),
    ("2-3 months before", "Review local races, ballot measures, and candidate platforms."),
    ("1-2 months before", "Request mail ballot if needed and confirm deadlines."),
    ("2-4 weeks before", "Make your voting plan: early voting, mail, or Election Day."),
    ("Election week", "Bring required ID/documents (if applicable) and vote."),
    ("After voting", "Track ballot status (mail voters) and verify it was accepted."),
]

STEPS = [
    ElectionStep(
        "Confirm eligibility",
        "Rules vary by state (age, citizenship, residency, and felony status).",
        "Check your state election website for official eligibility rules.",
    ),
    ElectionStep(
        "Register to vote",
        "Registration is required before you can cast a ballot in most elections.",
        "Register online, by mail, or in person before your state deadline.",
    ),
    ElectionStep(
        "Verify registration",
        "Clerical issues can remove or misplace active records.",
        "Use your state's voter lookup tool to confirm your active status.",
    ),
    ElectionStep(
        "Choose voting method",
        "Deadlines and procedures differ for in-person, early, and mail voting.",
        "Compare options and choose the one that best fits your schedule.",
    ),
    ElectionStep(
        "Prepare for ballot",
        "Being prepared reduces errors and time at the polling place.",
        "Preview a sample ballot, research races, and note your choices.",
    ),
    ElectionStep(
        "Cast your vote",
        "Votes count only when submitted correctly and on time.",
        "Follow instructions carefully, sign where required, and submit by deadline.",
    ),
]

FAQ = {
    "what id do i need": "ID requirements are state-specific. Some states require photo ID, some accept non-photo documents, and others do not require ID for most voters.",
    "can i vote by mail": "Most states allow some form of mail voting, but request and return deadlines vary. Always verify your county/state rules.",
    "what if i miss registration": "You may still be able to vote via same-day registration in certain states, or by provisional ballot in some cases.",
    "what is a provisional ballot": "A provisional ballot is used when your eligibility is in question at the polls. Election officials later verify and count it if valid.",
}


def print_header() -> None:
    print("\n=== Election Guide Assistant ===")
    print("Learn the election process in simple steps.")
    print("(General U.S. guidance; confirm details with your state election office.)\n")


def show_timeline() -> None:
    print("\nElection Timeline (typical):")
    for i, (period, task) in enumerate(TIMELINE, start=1):
        print(f"{i}. {period}: {task}")


def show_steps() -> None:
    print("\nStep-by-step voting process:")
    for i, step in enumerate(STEPS, start=1):
        print(f"\n{i}) {step.title}")
        print(f"   Why it matters: {step.why_it_matters}")
        print(f"   What to do: {step.action}")


def quick_plan() -> None:
    print("\nLet's build your quick voting plan.")
    state = input("What state are you voting in? ").strip() or "your state"
    method = input("Preferred method (in-person, early, mail, undecided): ").strip().lower()

    print("\nYour personalized checklist:")
    print(f"- Verify registration in {state}.")
    if method == "mail":
        print("- Request your mail ballot as early as possible.")
        print("- Track ballot mailing and return status.")
    elif method == "early":
        print("- Find early-voting locations and hours.")
        print("- Bring accepted ID/documents if required.")
    elif method == "in-person":
        print("- Confirm polling place and Election Day hours.")
        print("- Bring accepted ID/documents if required.")
    else:
        print("- Compare mail, early, and Election Day options for your county.")
    print("- Preview your sample ballot before voting.")
    print("- Submit your ballot before the official deadline.")


def ask_question() -> None:
    q = input("\nAsk a question (e.g., 'What ID do I need?'): ").strip().lower()
    for key, answer in FAQ.items():
        if key in q:
            print(f"\n{answer}")
            return
    print("\nI don't have that exact answer yet, but your state or county election office can confirm the official rule.")


def main() -> None:
    print_header()
    while True:
        print("Menu:")
        print("1) Understand election timeline")
        print("2) Learn step-by-step process")
        print("3) Build my quick voting plan")
        print("4) Ask a common question")
        print("5) Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_timeline()
        elif choice == "2":
            show_steps()
        elif choice == "3":
            quick_plan()
        elif choice == "4":
            ask_question()
        elif choice == "5":
            print("\nThanks for using Election Guide Assistant. Stay informed and vote!")
            break
        else:
            print("Please choose a valid option (1-5).")


if __name__ == "__main__":
    main()
