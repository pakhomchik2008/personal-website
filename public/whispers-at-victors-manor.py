"""
Whispers at Victor's Manor
FP016 Computer Science — Summative Assessment 2

A branching narrative mystery game built in Python.
The player investigates a suspicious death at Victor's Manor
and must uncover the truth through a series of choices.

Hlib
Wu
Sylvie
Melih

"""

# ── Standard / third-party imports ─────────────────────────────────────────
from tkinter import *
from tkinter import ttk, scrolledtext, messagebox
from PIL import Image, ImageTk
import heapq  # for clues
from collections import deque
from typing import List, Dict, Optional, Tuple  # useful one
import os

# -----------------------------WU part-------------------
# Folder that holds all background images.
# If the images sit next to the script, use the script directory directly.
# If they sit in a sibling folder named "cs photos", use that instead.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(SCRIPT_DIR, "cs photos")
if not os.path.isdir(IMAGE_DIR):
    IMAGE_DIR = SCRIPT_DIR


# --------------------WU Part-------------------


# =============================================================================
# SECTION 1 — DATA STRUCTURES(GLEB PART)
# =============================================================================

class StoryNode:
    def __init__(
            self,
            node_id: str,
            title: str,
            text: str,
            choices: Optional[List[Tuple[str, str]]] = None,
            clue: Optional[Dict] = None,
            is_ending: bool = False,
            ending_type: str = "",
            allow_rewind: bool = True,
            bg_image: str = "",
    ) -> None:  # means that all this stuff returns none
        self.node_id = node_id
        self.title = title
        self.text = text
        self.choices = choices if choices else []
        self.clue = clue
        self.is_ending = is_ending        # True if this node is a terminal/ending scene
        self.ending_type = ending_type    # category of ending (for ex: "Justice", "Silence")
        self.allow_rewind = allow_rewind    # whether the player can go back from this scene
        self.bg_image = bg_image  # filename for the bg image

    def __repr__(self) -> str:
        return f"StoryNode(id={self.node_id!r}, title={self.title!r})"  # !r means it adds '' very useful


class Stack:
    def __init__(self) -> None:
        self._data: List[str] = []    # internal list storing node IDs in visit order

    def push(self, item: str) -> None:
        self._data.append(item)

    def pop(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self._data[-1]

    # week 16 stuff

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def copy_list(self) -> List[str]:
        return list(self._data)  # added exactly for analysis and evidence panels!

    # alias kept for compatibility
    def to_list(self) -> List[str]:
        return self.copy_list()


class ClueHeap:  # added for counting clues
    def __init__(self) -> None:
        self.heap: List[Tuple] = []
        self.counter: int = 0

    def add_clue(self, clue_id: str, name: str, description: str,
                 importance: int, time_found: int) -> None:
        entry = (-importance, time_found, self.counter, clue_id, name, description)
        heapq.heappush(self.heap, entry)
        self.counter += 1
        print(f"Clue added to heap: {name!r} (importance={importance})")

    def get_sorted_clues(self) -> List[Dict]:
        copy_heap = list(self.heap)
        heapq.heapify(copy_heap)
        result = []
        while copy_heap:
            neg_imp, time_f, _, cid, name, desc = heapq.heappop(copy_heap)
            result.append({
                "id": cid, "name": name, "description": desc,
                "importance": -neg_imp, "time_found": time_f,
            })
        return result

    def size(self) -> int:
        return len(self.heap)


# =====================GLEB PART END==============================


# =============================================================================
# SECTION 2 — STORY GRAPH(Melih PART)
# =============================================================================

# This function builds the entire story graph by creating all the scenes and linking
# them together through player choices. The story always starts at S1 and splits into
# two main routes depending on what the player decides.

def build_story_graph() -> Dict[str, StoryNode]:
    """
    Creates all the scenes and connects them into a graph.
    The story starts at S1 and branches into two main routes
    (Security Guard or Sophia), each leading to different endings.
    Using a dict means we can look up any scene in O(1) by its id.
    """
    graph: Dict[str, StoryNode] = {}

    # --- Opening scenes ---
    graph["S1"] = StoryNode(
        "S1",
        "Arrival at Victor's Manor",
        (
            "You're an investigative journalist who's covered financial crime for years. "
            "A few months back, you published a piece questioning Victor's conglomerate "
            "— hinting at some sketchy financial statements. It got buried fast, "
            "but you never let it go.\n\n"
            "Late night. Your phone rings. A panicked female voice:\n"
            "  'If you still have doubts about that company, come to Victor's mansion tonight.\n"
            "   This might be your last chance to see the truth.'\n\n"
            "You head over. The front gate is half open. Garden lights are on. "
            "But the house? Silent. No servants. No guests. Just you and the quiet."
        ),
        choices=[("Enter the manor", "S2")],
        bg_image="Mansion.png",
    )

    graph["S2"] = StoryNode(
        "S2",
        "The Library — A Body on the Carpet",
        (
            "The library is quiet... too quiet. Victor lies on the floor, a fallen wine "
            "glass beside him. No struggle, no sign of forced entry. Just an oddly calm "
            "expression on his face.\n\n"
            "Two people are here with you:\n\n"
            "  • The Security Guard claims he just spotted someone climbing over the east wall.\n"
            "    Says it was probably a professional hitman. Very confident. Very specific.\n\n"
            "  • Sophia, Victor's assistant, looks shaken. She mentions Victor was worried "
            "    about a business partner and some 'financial mess' lately.\n\n"
            "You've got time to check out one lead first. Who's your priority?"
        ),
        choices=[
            ("Check the Security Guard's story first", "Q1_SECURITY"),
            ("Hear what Sophia has to say", "Q1_SOPHIA"),
        ],
        clue={
            "id": "C0",
            "name": "Victor's Body",
            "description": "Victor found dead beside a spilled wine glass. Possible poisoning.",
            "importance": 10,
        },
        bg_image="Library.png",
    )

    # --- Route 1: Security Branch ---
    graph["Q1_SECURITY"] = StoryNode(
        "Q1_SECURITY",
        "The Guard's Account",
        (
            "The guard tells you a shadowy figure climbed over the east wall and vanished "
            "into the garden. Claims Victor had 'lots of enemies' in business.\n\n"
            "His story is... oddly detailed. Almost like he rehearsed it.\n\n"
            "Time to pick your next move."
        ),
        choices=[
            ("Follow the garden trail he mentioned", "A3_GARDEN"),
            ("Check the CCTV system instead", "A3_CCTV"),
        ],
        clue={
            "id": "C1",
            "name": "Guard's Testimony",
            "description": "Guard claims a figure climbed the east wall. Story is vague but detailed.",
            "importance": 3,
        },
        allow_rewind=False,
        bg_image="Security guard.png",
    )

    graph["A3_GARDEN"] = StoryNode(
        "A3_GARDEN",
        "Garden Trail",
        (
            "You head to the garden near the east wall. Blurred footprints in the mud, "
            "some cigarette ends scattered around. Classic break-in vibes... maybe.\n\n"
            "But the footprints are smudged and the shoe type is super common. "
            "Nothing definitive here.\n\n"
            "Maybe the basement storage room has something better?"
        ),
        choices=[("Check the basement storage room", "A4_BASEMENT")],
        clue={
            "id": "C2",
            "name": "Garden Footprints",
            "description": "Blurred footprints and cigarette ends near the east wall. Inconclusive.",
            "importance": 2,
        },
        allow_rewind=True,
        bg_image="Garden trail.png",
    )

    graph["A4_BASEMENT"] = StoryNode(
        "A4_BASEMENT",
        "Underground Storage Room",
        (
            "Old tools, dusty boxes, years of neglect. Nothing useful here.\n\n"
            "You've been chasing the wrong lead. The 'outside killer' theory falls apart "
            "when there's nothing to back it up.\n\n"
            "Time to make a call on what to do with this mess."
        ),
        choices=[("Publish the article anyway", "ENDING_2A")],
        clue={
            "id": "C3",
            "name": "Empty Basement",
            "description": "Old tools and dust — no meaningful evidence found here.",
            "importance": 1,
        },
        bg_image="Basement.png",
    )

    graph["A3_CCTV"] = StoryNode(
        "A3_CCTV",
        "CCTV Control Room",
        (
            "You check the CCTV system with the guard. Something's off.\n\n"
            "The footage from the critical time window? Gone. Marked as 'file corrupted'. "
            "But every other hour is perfectly intact.\n\n"
            "That's not a glitch. Someone deleted that footage on purpose.\n\n"
            "Time to check those backup tapes."
        ),
        choices=[("Search the backup tapes", "A4_TAPES")],
        clue={
            "id": "C4",
            "name": "Deleted CCTV Footage",
            "description": "Critical time window deleted. Surrounding hours intact — deliberate tampering.",
            "importance": 5,
        },
        allow_rewind=True,
        bg_image="CCTV.png",
    )

    graph["A4_TAPES"] = StoryNode(
        "A4_TAPES",
        "Discarded Backup Tapes",
        (
            "Found a stack of discarded backup tapes under the desk. Someone did a thorough "
            "cleanup job here. Unfortunately, there's no way to recover what's on them.\n\n"
            "You're pretty sure someone inside the house is covering their tracks. "
            "But you've got nothing concrete.\n\n"
            "Time to make a decision with half the picture."
        ),
        choices=[("Publish what you have", "ENDING_2B")],
        clue={
            "id": "C5",
            "name": "Wiped Backup Tapes",
            "description": "Backup tapes erased. Evidence of tampering — but nothing is recoverable.",
            "importance": 4,
        },
        bg_image="CCTV room.png",
    )

    # --- Route 2: Sophia Brawhnch ---
    graph["Q1_SOPHIA"] = StoryNode(
        "Q1_SOPHIA",
        "Sophia's Revelation",
        (
            "Sophia leans in close. 'Victor was scared,' she says. 'Said if his business "
            "partner Adrian got exposed, he might do anything.'\n\n"
            "Victor was planning to confront Adrian after dinner that night. Probably about "
            "some financial irregularities he'd discovered.\n\n"
            "Sophia adds quietly: 'If this all comes out at once, a lot of people go down. "
            "Including innocent ones.'\n\n"
            "This isn't just a murder. It's a rabbit hole. Where do you start?"
        ),
        choices=[
            ("Track Adrian's movements first", "B3_PARKING"),
            ("Look into the company finances", "B3_FINANCE"),
        ],
        clue={
            "id": "C6",
            "name": "Sophia's Testimony",
            "description": "Victor feared business partner Adrian. A confrontation was planned that evening.",
            "importance": 7,
        },
        allow_rewind=False,
        bg_image="Sophia.png",
    )

    graph["B3_PARKING"] = StoryNode(
        "B3_PARKING",
        "Parking Lot Camera Records",
        (
            "You check the parking lot cameras. Something interesting shows up.\n\n"
            "Adrian's car left before dinner... but came back right during the estimated "
            "poisoning window. And no other vehicles entered during that time.\n\n"
            "That's suspicious timing. He was definitely here when it happened.\n\n"
            "Time to see what the kitchen records show."
        ),
        choices=[("Check the kitchen records", "B4_POISON")],
        clue={
            "id": "C7",
            "name": "Adrian's Car Log",
            "description": "Adrian's car returned during the estimated poisoning window.",
            "importance": 8,
        },
        allow_rewind=True,
        bg_image="Parking lot.png",
    )

    graph["B4_POISON"] = StoryNode(
        "B4_POISON",
        "Chemical Purchase Record",
        (
            "Found something in the kitchen storage: a bottle of specialized chemicals, "
            "locked in a separate cabinet. The purchase authorization? Signed by Adrian.\n\n"
            "This stuff is for lab use only. There's no legitimate reason for it to be "
            "anywhere near the kitchen.\n\n"
            "Motive. Opportunity. Means.\n"
            "The evidence chain is almost complete. Just one more piece..."
        ),
        choices=[("Open Victor's safe with Sophia", "B5_USB")],
        clue={
            "id": "C8",
            "name": "Chemical Purchase Log",
            "description": "Poison authorised by Adrian. Labelled for lab use — found near the kitchen.",
            "importance": 9,
        },
        allow_rewind=False,
        bg_image="Kitchen.png",
    )

    graph["B5_USB"] = StoryNode(
        "B5_USB",
        "Victor's USB Drive",
        (
            "Sophia leads you to Victor's private office. Hands shaking, she opens "
            "the wall safe and pulls out a USB drive.\n\n"
            "Inside: spreadsheets, emails, transfer records. Years of Adrian systematically "
            "draining the company through complex financial schemes.\n\n"
            "Victor knew. He'd been building a case. And Adrian must have found out.\n\n"
            "You now have everything:\n"
            "  • Motive: Adrian faced exposure for embezzlement.\n"
            "  • Opportunity: parking records place him at the scene.\n"
            "  • Means: his signature on the chemical purchase.\n"
            "  • Proof: the full financial trail on this USB.\n\n"
            "What do you do with this?"
        ),
        choices=[("Build the case and expose everything", "ENDING_1")],
        clue={
            "id": "C9",
            "name": "USB Financial Files",
            "description": "Proof of Adrian's embezzlement. Victor was building a case against him.",
            "importance": 10,
        },
        allow_rewind=False,
        bg_image="Victor’s private office.png",
    )

    graph["B3_FINANCE"] = StoryNode(
        "B3_FINANCE",
        "Finance Department",
        (
            "You visit the finance office late in the evening. The senior financial "
            "officer looks like he's about to pass out.\n\n"
            "  'If this comes out,' he says, 'the company collapses overnight. Hundreds "
            "of people who did nothing wrong get dragged down with it.'\n\n"
            "This is bigger than a murder. This is a whole system of corruption.\n\n"
            "Time to dig through the archives."
        ),
        choices=[("Head to the archive room", "B4_ARCHIVE")],
        clue={
            "id": "C10",
            "name": "Finance Officer's Warning",
            "description": "Corruption spans multiple executives and threatens hundreds of innocent employees.",
            "importance": 6,
        },
        allow_rewind=True,
        bg_image="Finance office.png",
    )

    graph["B4_ARCHIVE"] = StoryNode(
        "B4_ARCHIVE",
        "Underground Archive Room",
        (
            "Rows of filing cabinets stretch into darkness. Hours pass as you and Sophia "
            "go through emails, approvals, and money flow diagrams.\n\n"
            "It's worse than you thought. A years-long scheme involving multiple executives. "
            "Employee pensions, project budgets — all quietly siphoned off.\n\n"
            "You've got two options:\n\n"
            "  → Go public now: criminals get caught, but the company likely crashes. "
            "Thousands of innocent employees suffer first.\n\n"
            "  → Do nothing: the bad guys walk free, and the anonymous tip's last chance "
            "is completely wasted.\n\n"
            "But there's a third path..."
        ),
        choices=[("Send evidence anonymously and disappear", "ENDING_3")],
        clue={
            "id": "C11",
            "name": "Archive Documents",
            "description": "Extensive proof of a multi-executive financial crime network spanning years.",
            "importance": 8,
        },
        allow_rewind=False,
        bg_image="Archive room.png",
    )

    # --- Endings ---
    graph["ENDING_1"] = StoryNode(
        "ENDING_1",
        "Ending 1 — Justice",
        (
            "You compile everything and send it to the police and three major news outlets "
            "at the same time.\n\n"
            "Chaos erupts. Adrian is arrested within 48 hours. Executives are hauled "
            "in front of regulators. The company's stock price goes into freefall.\n\n"
            "It's messy. It's ugly. Thousands of shareholders lose money. But the truth "
            "is finally, irreversibly out there.\n\n"
            "The main culprit falls in broad daylight.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "  JUSTICE — The truth came out. The dramatic way.\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        is_ending=True,
        ending_type="Justice",
    )

    graph["ENDING_2A"] = StoryNode(
        "ENDING_2A",
        "Ending 2A — Silence",
        (
            "You publish the article about a professional hitman. "
            "With no real evidence, the police file it as 'suspected external homicide' "
            "and move on.\n\n"
            "The real killer is untouched. The financial crimes keep happening. "
            "You worked hard — but you were chasing the wrong lead.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "  SILENCE — The truth gets buried under a convenient narrative.\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        is_ending=True,
        ending_type="Silence",
    )

    graph["ENDING_2B"] = StoryNode(
        "ENDING_2B",
        "Ending 2B — Silence",
        (
            "You publish what you found: the missing footage, the wiped tapes, the guard's "
            "story that doesn't quite add up.\n\n"
            "Some detectives nod appreciatively. But without hard evidence? Nothing changes.\n\n"
            "You saw through part of the lie. But seeing it and proving it are different things.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "  SILENCE — You saw the lie. But couldn't break it open.\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        is_ending=True,
        ending_type="Silence",
    )

    graph["ENDING_3"] = StoryNode(
        "ENDING_3",
        "Ending 3 — Vanishing Truth",
        (
            "You carefully package only the core evidence — critical emails, signed "
            "authorizations, money-flow diagrams — and send it anonymously to financial "
            "regulators and the police's anti-corruption unit.\n\n"
            "You hold back the most explosive data, the full scale of the losses, to "
            "prevent market panic that would destroy innocent people's livelihoods.\n\n"
            "Then you wipe every trace of your involvement, leave the city, and refuse "
            "every interview request.\n\n"
            "Months later: the case reopens. Regulators announce an investigation. The "
            "media gets 'official' leaks. The truth comes out piece by piece.\n\n"
            "No one knows it started with one anonymous package from a journalist who "
            "chose to vanish from her own story.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "  VANISHING TRUTH — Justice unfolds slowly. You disappear.\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        is_ending=True,
        ending_type="Vanishing",
    )

    return graph


# =============================================================================
# SECTION 3 — ALGORITHMS(ZhengJiang PART)
# =============================================================================

def dfs_reachability(graph: Dict[str, StoryNode], start: str):
    # Depth-First Search (DFS)
    # Visits all reachable scenes from the start node
    # Uses a stack to keep track of which scenes to visit next
    # A scene is "reachable" if we can get to it from the start by following choices

    try:
        visited = {}  # keeps track of which scenes we've already visited
        stack = [start]  # scenes we still need to explore

        while stack:  # keep going until there's nothing left to check
            node_id = stack.pop()  # grab the next scene from the stack

            if node_id in visited:  # skip if we already checked this one
                continue

            visited[node_id] = True  # mark as visited

            # add all connected scenes to the stack
            if node_id in graph:
                for _, next_id in graph[node_id].choices:
                    if next_id not in visited:
                        stack.append(next_id)

        return visited
    except Exception as e:
        print(f"Error in dfs_reachability: {e}")
        return {}  # return empty dict if something goes wrong


def bfs_shortest_path(graph: Dict[str, StoryNode], start: str, target: str):
    # Breadth-First Search (BFS)
    # Finds the shortest path from start to target (fewest choices needed)
    # Uses a queue so we explore all scenes at the current level before moving deeper

    try:
        if start == target:  # already at the target
            return [start]

        # queue stores (scene_id, path_to_get_here)
        queue = deque([(start, [start])])
        visited = {start}  # keep track of visited scenes to avoid loops

        while queue:
            node_id, path = queue.popleft()  # get the next scene to check

            if node_id not in graph:  # skip if scene doesn't exist
                continue

            # check all choices from this scene
            for _, next_id in graph[node_id].choices:
                if next_id == target:  # found the target, return the path
                    return path + [next_id]

                if next_id not in visited:  # if not visited yet, add to queue
                    visited.add(next_id)
                    queue.append((next_id, path + [next_id]))

        return []  # no path found
    except Exception as e:
        print(f"Error in bfs_shortest_path: {e}")
        return []  # return empty list if something goes wrong


def insertion_sort_clues(clues: List[Dict]):
    # Sorts clues by the step they were discovered (time_found)
    # Goes through the list one by one and puts each item in its correct position
    # Simple but not the fastest for large lists

    try:
        result = list(clues)  # make a copy so we don't change the original
        n = len(result)

        for i in range(1, n):  # start from the second item
            key = result[i]  # this is the item we want to place
            j = i - 1

            # move all items that were found later than the key, one position to the right
            while j >= 0 and result[j]["time_found"] > key["time_found"]:
                result[j + 1] = result[j]
                j -= 1

            result[j + 1] = key  # put the key in its correct position

        return result
    except Exception as e:
        print(f"Error in insertion_sort_clues: {e}")
        return clues  # return original list if something goes wrong


def topological_sort(dependencies: Dict[str, List[str]]):
    # Kahn's algorithm for topological sorting
    # Puts clues in an order where each clue comes after all the clues it depends on
    # Used to figure out a valid order for collecting all clues

    try:
        # collect all unique clue IDs
        all_nodes = set(dependencies.keys())
        for children in dependencies.values():
            all_nodes.update(children)

        # count how many prerequisites each node has (in_degree)
        in_degree = {node: 0 for node in all_nodes}
        for node, children in dependencies.items():
            for child in children:
                in_degree[child] += 1

        # start with nodes that have no prerequisites
        queue = deque(sorted(n for n in all_nodes if in_degree[n] == 0))
        result = []

        while queue:
            node = queue.popleft()  # take a node with no remaining prerequisites
            result.append(node)

            # for each node that depends on this one, reduce its prerequisite count
            for child in sorted(dependencies.get(node, [])):
                in_degree[child] -= 1
                if in_degree[child] == 0:  # all prerequisites satisfied, add to queue
                    queue.append(child)

        # if we didn't process all nodes, there's a cycle (shouldn't happen in a proper story)
        if len(result) != len(all_nodes):
            print("topological_sort: cycle detected, returning empty list")
            return []

        return result
    except Exception as e:
        print(f"Error in topological_sort: {e}")
        return []  # return empty list if something goes wrong


def get_clue_dependencies():
    # Defines which clues must be found before others
    # Key = clue ID, Value = list of clues that depend on it
    # For example: C0 must be found before C6 and C1
    return {
        "C0": ["C6", "C1"],
        "C1": ["C2", "C4"],
        "C2": ["C3"],
        "C4": ["C5"],
        "C6": ["C7", "C10"],
        "C7": ["C8"],
        "C8": ["C9"],
        "C10": ["C11"],
        "C3": [],
        "C5": [],
        "C9": [],
        "C11": [],
    }


# =============================================================================
# SECTION 4 — GAME ENGINE(ZhengJiang PART)
# =============================================================================

class GameEngine:
    # This is the core game engine that manages all game state
    # Think of this as the "brain" of the game
    # It keeps track of where the player is, the path taken (for rewinding),
    # clues discovered, and how many steps have been taken
    # The UI layer calls methods here to make choices, rewind, etc.

    def __init__(self):
        # Load the entire story graph (all scenes and connections)
        self.story_graph = build_story_graph()

        # Start at the first scene (S1)
        self.current_node_id = "S1"

        # Stack to keep track of visited scenes (for rewinding)
        self.rewind_stack = Stack()

        # Priority queue to organize clues by importance
        self.clue_heap = ClueHeap()

        # List to keep track of all discovered clues in order
        self.discovered_clues = []

        # Counter to track how many choices the player has made
        self.step_counter = 0

        # Collect any clue from the starting scene
        self._collect_clue("S1")

    def get_current_node(self):
        # Get the StoryNode object for the current scene
        return self.story_graph[self.current_node_id]

    def get_path_history(self):
        # Get a list of all scenes visited so far (for display purposes)
        return self.rewind_stack.to_list()

    def make_choice(self, choice_index):
        # Make a choice and advance to the next scene
        # choice_index is the index of the choice the player made (0, 1, etc.)
        # Returns True if the choice was valid and we moved to a new scene

        try:
            node = self.get_current_node()

            # Validate the choice index — make sure it's within bounds
            if choice_index < 0 or choice_index >= len(node.choices):
                print(f"Invalid choice index: {choice_index} (only {len(node.choices)} choices available)")
                return False

            # Save the current scene to the rewind stack before moving
            self.rewind_stack.push(self.current_node_id)

            # Get the ID of the next scene from the chosen option
            _, next_id = node.choices[choice_index]

            # Move to the next scene
            self.current_node_id = next_id

            # Increment the step counter
            self.step_counter += 1

            # Collect any clue from the new scene
            self._collect_clue(next_id)

            print(f"Moved to {next_id} (step {self.step_counter})")
            return True
        except Exception as e:
            print(f"Error in make_choice: {e}")
            return False  # return False if something goes wrong

    def can_rewind(self):
        # Check if the player can go back to a previous scene
        # Returns True if rewinding is allowed, False otherwise

        # Can't rewind if there's nowhere to go back to
        if self.rewind_stack.is_empty():
            return False

        # Can't rewind from an ending scene
        current_node = self.get_current_node()
        if current_node.is_ending:
            return False

        # Some scenes explicitly disallow rewinding
        if not current_node.allow_rewind:
            return False

        # All checks passed — rewinding is allowed
        return True

    def rewind(self):
        # Go back to the previous scene
        # Returns True if we successfully rewound, False otherwise

        try:
            # Check if rewinding is allowed
            if not self.can_rewind():
                print("Cannot rewind from this scene")
                return False

            # Get the previous scene from the stack
            prev_id = self.rewind_stack.pop()

            # Just in case the stack was emptied between can_rewind() and pop()
            if prev_id is None:
                return False

            # Move back to the previous scene
            self.current_node_id = prev_id

            print(f"Rewound to {prev_id}")
            return True
        except Exception as e:
            print(f"Error in rewind: {e}")
            return False  # return False if something goes wrong

    def restart(self):
        # Reset the game to its initial state

        # Go back to the first scene
        self.current_node_id = "S1"

        # Clear the rewind stack
        self.rewind_stack = Stack()

        # Clear the clue heap
        self.clue_heap = ClueHeap()

        # Clear the discovered clues list
        self.discovered_clues = []

        # Reset the step counter
        self.step_counter = 0

        # Collect the starting clue again
        self._collect_clue("S1")

        print("Game restarted")

    def _collect_clue(self, node_id):
        # Collect a clue from a scene if it has one (and we haven't collected it yet)
        # node_id is the ID of the scene to check for clues

        try:
            # Get the scene from the story graph
            node = self.story_graph.get(node_id)

            # Check if the scene exists and has a clue
            if node and node.clue:
                clue = node.clue

                # Check if we've already collected this clue
                existing_ids = {c["id"] for c in self.discovered_clues}

                if clue["id"] not in existing_ids:
                    # Add to priority heap (sorted by importance)
                    self.clue_heap.add_clue(
                        clue["id"],
                        clue["name"],
                        clue["description"],
                        clue["importance"],
                        self.step_counter,
                    )

                    # Add to discovered list with timestamp
                    self.discovered_clues.append({**clue, "time_found": self.step_counter})
        except Exception as e:
            print(f"Error in _collect_clue: {e}")
            # just pass if something goes wrong

    def get_prioritised_clues(self):
        # Get clues sorted by importance (most important first)
        return self.clue_heap.get_sorted_clues()

    def get_timeline_clues(self):
        # Get clues sorted by the order they were discovered
        return insertion_sort_clues(self.discovered_clues)

    def run_dfs_analysis(self):
        # Run a Depth-First Search analysis to check which scenes are reachable
        # Returns a dictionary with statistics about scene reachability

        visited = dfs_reachability(self.story_graph, "S1")

        # Check which endings are reachable
        all_endings = ["ENDING_1", "ENDING_2A", "ENDING_2B", "ENDING_3"]
        reachable_endings = [e for e in all_endings if visited.get(e, False)]

        # Find any scenes that can't be reached
        dead_scenes = [nid for nid in self.story_graph if not visited.get(nid, False)]

        print(f"DFS: visited {len(visited)} nodes, {len(reachable_endings)} endings reachable")

        return {
            "total_visited": len(visited),
            "reachable_endings": reachable_endings,
            "dead_scenes": dead_scenes,
        }

    def run_bfs_analysis(self):
        # Run a Breadth-First Search analysis to find shortest paths to endings
        # Returns a dictionary with shortest path information for each ending

        endings = {
            "Justice (Ending 1)": "ENDING_1",
            "Silence A (Ending 2A)": "ENDING_2A",
            "Silence B (Ending 2B)": "ENDING_2B",
            "Vanishing Truth (Ending 3)": "ENDING_3",
        }

        results = {}
        for label, eid in endings.items():
            # Find the shortest path to this ending
            path = bfs_shortest_path(self.story_graph, "S1", eid)

            # Calculate steps (number of choices = path length - 1)
            steps = len(path) - 1 if path else -1

            results[label] = {
                "steps": steps,
                "path": " -> ".join(path) if path else "Unreachable",
            }

            print(f"BFS to {eid}: {steps} steps")

        return results

    def run_topo_analysis(self):
        # Run a topological sort analysis on clue dependencies
        # Returns a list of clue IDs in valid discovery order

        deps = get_clue_dependencies()
        result = topological_sort(deps)

        print(f"Topo sort result: {result}")
        return result


# =====================ZhengJiang PART END==============================

# =============================================================================
# SECTION 5 — POPUP WINDOWS  (Evidence Panel + Algorithm Analysis) (GLEB PART)
# =============================================================================

# Shared colour / font constants for popup windows
_BG_DARK = "#111111"
_BG_PANEL = "#1a1a1a"
_FG_MAIN = "#ffffff"
_FG_DIM = "#aaaaaa"
_ACCENT = "#e6a817"
_ACCENT2 = "#58a6ff"
_SUCCESS = "#3fb950"
_BORDER = "#333333"
_FONT_MONO = ("Courier", 14)
_FONT_SMALL = ("Arial", 15)
_FONT_BODY = ("Arial", 25)


class AnalysisWindow:

    # Separate window showing the algorithm analysis results.
    # Four tabs: DFS reachability, BFS shortest paths, insertion sort timeline, and topological clue order.

    def __init__(self, parent: Widget, engine: GameEngine) -> None:
        self.win = Toplevel(parent)
        self.win.title("Algorithm Analysis — Whispers at Victor's Manor")
        self.win.configure(bg=_BG_DARK)
        self.win.geometry("720x580")
        self.win.resizable(True, True)
        self.win.protocol("WM_DELETE_WINDOW", self._on_close)
        self._build(engine)

    def _on_close(self) -> None:
        global _analysis_window
        _analysis_window = None # ensure only one instance of each window exists at a time.
        self.win.destroy()

    def _build(self,
               engine: GameEngine) -> None:  # here you can change label size and font of literally everything in analysis
        Label(
            self.win, text="Algorithm Analysis Dashboard",
            font=("Arial", 25, "bold"), bg=_BG_DARK, fg=_ACCENT,
        ).pack(pady=(16, 4))
        # Create tabbed notebook
        nb = ttk.Notebook(self.win)
        nb.pack(fill="both", expand=True, padx=16, pady=8)

        # Style the notebook tabs to match the dark theme
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook", background=_BG_DARK, borderwidth=0)
        style.configure("TNotebook.Tab", background=_BG_PANEL, foreground=_FG_DIM,
                        padding=[12, 6], font=_FONT_SMALL)
        style.map("TNotebook.Tab",
                  background=[("selected", "#2a2a2a")],
                  foreground=[("selected", _ACCENT)])

        # Tab 1 — Reachability
        # Shows total reachable nodes and which endings can be accessed
        f1 = self._make_frame(nb)
        nb.add(f1, text=" DFS Reachability  ")
        dfs_data = engine.run_dfs_analysis()
        lines = [
            f"Depth-First Search from S1\n{'─' * 50}",
            f"Total nodes visited:  {dfs_data['total_visited']}",
            f"Reachable endings:    {len(dfs_data['reachable_endings'])} / 4",
            "",
        ]
        for i in dfs_data["reachable_endings"]:
            lines.append(f"  v  {i}")
        if dfs_data["dead_scenes"]:
            lines += ["", "Dead scenes (unreachable):"]
            for e in dfs_data["dead_scenes"]:
                lines.append(f"  x  {e}")
        else:
            lines += ["", "No dead scenes — all nodes are reachable."]
        self._add_text(f1, "\n".join(lines))

        # Tab 2 — Shortest Paths
        # Displays the minimum number of decisions to reach each ending
        f2 = self._make_frame(nb)
        nb.add(f2, text=" BFS Shortest Paths  ")
        bfs_data = engine.run_bfs_analysis()
        lines2 = [f"Breadth-First Search from S1\n{'─' * 50}", ""]
        for label, info in bfs_data.items():
            lines2.append(f"> {label}")
            lines2.append(f"  Decisions required: {info['steps']}")
            parts = info["path"].split(" -> ")
            wrapped = "\n    ".join(" -> ".join(parts[i:i + 3]) for i in range(0, len(parts), 3))
            lines2.append(f"  Path: {wrapped}")
            lines2.append("")
        self._add_text(f2, "\n".join(lines2))

        # Tab 3 — Insertion Sort (Timeline)
        # Shows clues using insertion sort
        f3 = self._make_frame(nb)
        nb.add(f3, text="  Evidence Timeline  ")
        sorted_clues = engine.get_timeline_clues()
        lines3 = [
            f"Insertion Sort — Clues in Discovery Order\n{'─' * 50}",
            f"Total clues found so far: {len(sorted_clues)}",
            "",
        ]
        if not sorted_clues:
            lines3.append("(No clues discovered yet — play the game to collect evidence.)")
        else:
            for c in sorted_clues:
                lines3.append(f"  Step {c['time_found']:>2} | [{c['id']}] {c['name']}")
                lines3.append(f"         Importance: {c['importance']}/10")
                lines3.append(f"         {c['description']}")
                lines3.append("")
        self._add_text(f3, "\n".join(lines3))

        # Tab 4 — Topological Sort
        # Displays the valid logical order for discovering clues based on dependencies
        f4 = self._make_frame(nb)
        nb.add(f4, text="  Clue Dependency Order  ")
        topo = engine.run_topo_analysis() # Mapping clue IDs to human-readable names for display
        clue_names = {
            "C0": "Victor's Body", "C1": "Guard's Testimony",
            "C2": "Garden Footprints", "C3": "Empty Basement",
            "C4": "Deleted CCTV Footage", "C5": "Wiped Backup Tapes",
            "C6": "Sophia's Testimony", "C7": "Adrian's Car Log",
            "C8": "Chemical Purchase Log", "C9": "USB Financial Files",
            "C10": "Finance Officer Warning", "C11": "Archive Documents",
        }
        lines4 = [
            f"Kahn's Topological Sort — Clue Dependency DAG\n{'─' * 50}",
            "Valid logical discovery order (A -> B means A must precede B):\n",
        ]
        if not topo:
            lines4.append("Cycle detected in dependency graph!")
        else:
            for i, cid in enumerate(topo, 1):
                name = clue_names.get(cid, cid)
                lines4.append(f"  {i:>2}. {cid:<5} — {name}")
         # Show the main dependency chains for quick reference
        lines4 += [
            "",
            "Key dependency chains:",
            "  C0 -> C6 -> C7 -> C8 -> C9  (Justice path)",
            "  C0 -> C6 -> C10 -> C11      (Vanishing path)",
            "  C0 -> C1 -> C4 -> C5        (Silence B path)",
            "  C0 -> C1 -> C2 -> C3        (Silence A path)",
        ]
        self._add_text(f4, "\n".join(lines4))

    @staticmethod
    def _make_frame(parent: ttk.Notebook) -> Frame:  # creates an empty dark frame for a tab
        f = Frame(parent, bg="#222222")
        f.columnconfigure(0, weight=1)
        f.rowconfigure(0, weight=1)
        return f

    @staticmethod
    def _add_text(frame: Frame, content: str) -> None:  # puts a read-only scrollable text box inside that frame
        txt = scrolledtext.ScrolledText(
            frame, bg="#222222", fg=_FG_MAIN,
            font=_FONT_MONO, wrap=WORD,
            relief="flat", borderwidth=0,
            padx=12, pady=12,
        )
        txt.insert("1.0", content)
        txt.configure(state="disabled")    # make read-only after inserting
        txt.pack(fill="both", expand=True)


class EvidencePanel(Toplevel):

    # Secondary window showing discovered clues.
    # Can be sorted by priority (heap) or by discovery time (insertion sort).
    # same patern as for analysis window just a little bit different (add text  radiobutton text_pack,heap and stuff) but i want to add one more window ahah

    def __init__(self, parent: Widget, engine: GameEngine) -> None:
        super().__init__(parent)
        self.engine = engine
        self.title("Evidence Panel")
        self.configure(bg=_BG_DARK)
        self.geometry("480x520")
        self.resizable(True, True)
        self._sort_mode = StringVar(value="priority") # default to importance-based sorting
        self._build()
        self.refresh()

    def _build(self) -> None:
        Label(
            self, text="Emma's Evidence Panel",
            font=("Arial", 14, "bold"), bg=_BG_DARK, fg=_ACCENT,
        ).pack(pady=(14, 4))


        # Radio buttons to toggle between priority and timeline sort modes
        ctrl = Frame(self, bg=_BG_DARK)
        ctrl.pack()

        for text, val in [("Priority order", "priority"), ("Timeline order", "timeline")]:
            Radiobutton(
                ctrl, text=text, variable=self._sort_mode, value=val,
                command=self.refresh,
                bg=_BG_DARK, fg=_FG_DIM, selectcolor=_BG_PANEL,
                activebackground=_BG_DARK, activeforeground=_FG_MAIN,
                font=_FONT_SMALL,
            ).pack(side=LEFT, padx=8)


        # Scrollable text area for displaying clue details
        self._text = scrolledtext.ScrolledText(
            self, bg="#222222", fg=_FG_MAIN,
            font=_FONT_BODY, wrap=WORD,
            relief="flat", borderwidth=0,
            padx=14, pady=10,
        )
        self._text.pack(fill="both", expand=True, padx=14, pady=(6, 14))

    def refresh(self) -> None:
        if self._sort_mode.get() == "priority":
            clues = self.engine.get_prioritised_clues()
            header = "Ordered by importance (most critical first):\n\n"
        else:
            clues = self.engine.get_timeline_clues()
            header = "Ordered by discovery time (insertion sort):\n\n"

         # Clear and repopulate the text widget
        self._text.configure(state="normal")
        self._text.delete("1.0", END)

        if not clues:
            self._text.insert(END, "No clues discovered yet.")
        else:
            self._text.insert(END, header)
            for c in clues:
                self._text.insert(
                    END,
                    f"[{c['id']}]  {c['name']}  (importance: {c['importance']}/10)\n",
                )
                self._text.insert(END, f"     {c['description']}\n\n")

        self._text.configure(state="disabled")    # lock text after updating


# =============================================================================
# SECTION 6 — MAIN GUI  (SYLVIE PART)
# =============================================================================

#Initialize variables of GUI
engine = GameEngine()
_game_started = False

_evidence_window = None
_analysis_window = None
_menu_title = None
_menu_start_btn = None
_menu_continue_btn = None
_menu_credits_btn = None
_continue_button = None

# main window
root = Tk()
root.title("Whispers at Victor's Manor")
root.geometry("1200x800+100+0")
root.configure(bg="#111111")

#Make the window appear in front of other windows
root.lift()
root.attributes("-topmost", True)
#Enable the ability to switch to another interface and bring it to the front after 100 milliseconds.
root.after(100, lambda: root.attributes("-topmost", False))
root.focus_force()

#Create all widgets
# toolbar：used to display gameplay status information,including rewind availability and player progress.
toolbar = Frame(root, bg="#1a1a1a")
toolbar.pack(fill=X, side=TOP)

Label(
    toolbar,
    text="WHISPERS AT VICTOR'S MANOR",
    font=("Arial", 11, "bold"),
    bg="#1a1a1a",
    fg="#e6a817",
).pack(side=LEFT, padx=16, pady=8)

_step_label = Label(
    toolbar,
    text="",
    font=("Arial", 9),
    bg="#1a1a1a",
    fg="#888888",
)
_step_label.pack(side=LEFT, padx=4)

_tb_btn = {
    "relief": "solid",
    "cursor": "hand2",
    "padx": 10,
    "pady": 4,
    "font": ("Arial", 9, "bold"),
    "bg": "#c8a96e",
    "fg": "#1a1a2e",
    "activebackground": "#e8c98e",
    "activeforeground": "#1a1a2e",
    "bd": 1,
}

Button(toolbar, text="Restart",
       command=lambda: _on_restart(), **_tb_btn).pack(side=RIGHT, padx=6, pady=6)

Button(toolbar, text="Analysis",
       command=lambda: _open_analysis(), **_tb_btn).pack(side=RIGHT, padx=2, pady=6)

Button(toolbar, text="Evidence",
       command=lambda: _open_evidence(), **_tb_btn).pack(side=RIGHT, padx=2, pady=6)

_rewind_btn = Button(toolbar, text="Rewind",
                     command=lambda: _on_rewind(), **_tb_btn)
_rewind_btn.pack(side=RIGHT, padx=2, pady=6)

Frame(root, bg="#e6a817", height=2).pack(fill=X)

# status bar
status_bar = Frame(root, bg="#1a1a1a")
status_bar.pack(fill=X, side=BOTTOM)

_path_label = Label(
    status_bar,
    text="Path: —",
    font=("Arial", 9),
    bg="#1a1a1a",
    fg="#888888",
)
_path_label.pack(side=LEFT, padx=16, pady=5)

_clue_count_label = Label(
    status_bar,
    text="Clues: 0",
    font=("Arial", 9),
    bg="#1a1a1a",
    fg="#888888",
)
_clue_count_label.pack(side=RIGHT, padx=16, pady=5)

#Store the image as the background and prevent Tkinter from automatically recycling the image.
bg_photo = None
background_label = Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# story widgets
title_label = Label(
    root,
    text="",
    font=("Arial", 28, "bold"),
    bg="#1a1a2e",
    fg="#f5deb3",
    padx=20,
    pady=8,
)

story_text = Text(
    root,
    width=90,
    height=9,
    font=("Arial", 14),
    wrap=WORD,
    bg="#1a1a2e",
    fg="#f5deb3",
    insertbackground="#f5deb3",
    relief="solid",
    bd=1,
    padx=10,
    pady=15,
)

main_button = Button(
    root,
    text="",
    font=("Arial", 15, "bold"),
    width=22,
    height=2,
    wraplength=680,
    bg="#c8a96e",
    fg="#1a1a2e",
    activebackground="#e8c98e",
    activeforeground="#1a1a2e",
    relief="solid",
    bd=2,
    cursor="hand2",
)

choice_frame = Frame(root, bg="#1a1a2e")

choice_button1 = Button(
    choice_frame,
    text="",
    font=("Arial", 12, "bold"),
    width=48,
    height=3,
    wraplength=700,
    justify=LEFT,
    anchor=W,
    bg="#c8a96e",
    fg="#1a1a2e",
    activebackground="#e8c98e",
    activeforeground="#1a1a2e",
    relief="solid",
    bd=2,
    cursor="hand2",
)

choice_button2 = Button(
    choice_frame,
    text="",
    font=("Arial", 12, "bold"),
    width=48,
    height=3,
    wraplength=700,
    justify=LEFT,
    anchor=W,
    bg="#c8a96e",
    fg="#1a1a2e",
    activebackground="#e8c98e",
    activeforeground="#1a1a2e",
    relief="solid",
    bd=2,
    cursor="hand2",
)

ending_frame = Frame(root, bg="#1a1a2e")

analyze_button = Button(
    ending_frame,
    text="Analyze",
    font=("Arial", 14, "bold"),
    width=12,
    height=2,
    bg="#c8a96e",
    fg="#1a1a2e",
    activebackground="#e8c98e",
    activeforeground="#1a1a2e",
    relief="solid",
    bd=2,
    cursor="hand2",
)

restart_button = Button(
    ending_frame,
    text="Restart",
    font=("Arial", 14, "bold"),
    width=12,
    height=2,
    bg="#c8a96e",
    fg="#1a1a2e",
    activebackground="#e8c98e",
    activeforeground="#1a1a2e",
    relief="solid",
    bd=2,
    cursor="hand2",
)

exit_button = Button(
    ending_frame,
    text="Exit",
    font=("Arial", 14, "bold"),
    width=12,
    height=2,
    bg="#8b2020",
    fg="#ffffff",
    activebackground="#a83030",
    activeforeground="#ffffff",
    relief="solid",
    bd=2,
    cursor="hand2",
)

menu_button = Button(
    root,
    text="Menu",
    font=("Arial", 12, "bold"),
    width=10,
    height=1,
    bg="#c8a96e",
    fg="#1a1a2e",
    activebackground="#e8c98e",
    activeforeground="#1a1a2e",
    relief="solid",
    bd=2,
    cursor="hand2",
)

_clue_banner = Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#1a2a1a",
    fg="#3fb950",
    anchor=W,
    padx=14,
    pady=4,
)


# =============================================================================
# SECTION 7 — FUNCTIONS  (SYLVIE PART)
# =============================================================================

def set_background(filename):
    global bg_photo

    if not filename:
        return

    full_path = os.path.join(IMAGE_DIR, filename)
    # Prevent the graphical user interface from crashing due to an invalid background image path or a missing file.
    if not os.path.exists(full_path):
        print("Background not found:", full_path)
        return

    image = Image.open(full_path)
    image = image.resize((1200, 800))
    bg_photo = ImageTk.PhotoImage(image)#Convert a PIL image to a Tkinter-compatible image object that can be displayed.

    background_label.config(image=bg_photo)
    background_label.lower()


def clear_screen():
    title_label.pack_forget()
    title_label.place_forget()

    story_text.pack_forget()
    story_text.place_forget()

    main_button.pack_forget()
    main_button.place_forget()

    choice_frame.pack_forget()
    choice_frame.place_forget()
    choice_button1.pack_forget()
    choice_button1.place_forget()
    choice_button2.pack_forget()
    choice_button2.place_forget()

    ending_frame.pack_forget()
    ending_frame.place_forget()
    analyze_button.pack_forget()
    restart_button.pack_forget()
    exit_button.pack_forget()

    _clue_banner.pack_forget()
    _clue_banner.place_forget()

    menu_button.pack_forget()
    menu_button.place_forget()

#Hide all main menu components before switching to the game interface.
def hide_main_menu():
    if _menu_title is not None:
        _menu_title.place_forget()
    if _menu_start_btn is not None:
        _menu_start_btn.place_forget()
    if _menu_continue_btn is not None:
        _menu_continue_btn.place_forget()
    if _menu_credits_btn is not None:
        _menu_credits_btn.place_forget()


def show_main_menu():
    global _menu_title, _menu_start_btn, _menu_continue_btn
    global _menu_credits_btn, _continue_button

    clear_screen()
    hide_main_menu()
    set_background("Mansion.png")

    toolbar.pack_forget()
    status_bar.pack_forget()

    if _menu_title is None:
        _menu_title = Label(
            root,
            text="Whispers at Victor’s Manor",
            font=("Arial", 36, "bold"),
            bg="#c8a96e",
            fg="#1a1a2e",
            pady=15,
            relief="solid",
            bd=2,
        )

        _menu_start_btn = Button(
            root,
            text="New Game",
            font=("Arial", 16, "bold"),
            width=20,
            height=2,
            bg="#c8a96e",
            fg="#1a1a2e",
            activebackground="#e8c98e",
            activeforeground="#1a1a2e",
            relief="solid",
            bd=2,
            cursor="hand2",
            command=_start_new_game,
        )

        _menu_continue_btn = Button(
            root,
            text="Continue Game",
            font=("Arial", 16, "bold"),
            width=20,
            height=2,
            bg="#c8a96e",
            fg="#1a1a2e",
            activebackground="#e8c98e",
            activeforeground="#1a1a2e",
            relief="solid",
            bd=2,
            cursor="hand2",
            command=_continue_game,
            state=DISABLED,
        )

        _continue_button = _menu_continue_btn

        _menu_credits_btn = Button(
            root,
            text="Credits",
            font=("Arial", 14, "bold"),
            width=15,
            height=1,
            bg="#c8a96e",
            fg="#1a1a2e",
            activebackground="#e8c98e",
            activeforeground="#1a1a2e",
            relief="solid",
            bd=2,
            cursor="hand2",
            command=_show_credits,
        )

    _menu_title.place(relx=0.5, rely=0.25, anchor=CENTER)
    _menu_start_btn.place(relx=0.5, rely=0.45, anchor=CENTER)
    _menu_continue_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
    _menu_credits_btn.place(relx=0.5, rely=0.75, anchor=CENTER)

    if _game_started:
        _menu_continue_btn.config(state=NORMAL)
    else:
        _menu_continue_btn.config(state=DISABLED)

    root.lift()
    root.attributes("-topmost", True)
    root.after(100, lambda: root.attributes("-topmost", False))
    root.focus_force()#Force the root window to become the currently active window


def _start_new_game():
    global _game_started

    engine.restart()
    _game_started = True

    if _continue_button is not None:
        _continue_button.config(state=NORMAL)

    show_page()


def _continue_game():
    show_page()


def _show_credits():
    credits_win = Toplevel(root)#Create an independent window to display credits
    credits_win.title("Credits")
    credits_win.geometry("500x400")
    credits_win.configure(bg="#1a1a2e")
    credits_win.resizable(False, False)

    title = Label(
        credits_win,
        text="Credits",
        font=("Arial", 20, "bold"),
        bg="#c8a96e",
        fg="#1a1a2e",
        pady=10,
        relief="solid",
        bd=2,
    )
    title.pack(pady=(20, 10))

    credits_text = Label(
        credits_win,
        font=("Arial", 12),
        bg="#c8a96e",
        fg="#1a1a2e",
        text=(
            "Game Development Team:\n\n"
            "• Engine and Algorithm Developer: Zhengjiang\n"
            "• Data Structures: Gleb\n"
            "• Story Graph: Melih\n"
            "• UI Design: Shuyi\n\n"
            "We are grateful for your playing:)"
        ),
        justify=LEFT,
        anchor=W,
        padx=20,
        pady=15,
        relief="solid",
        bd=2,
    )
    credits_text.pack(pady=(10, 20), fill=X, padx=20)

    close_button = Button(
        credits_win,
        text="Close",
        font=("Arial", 12, "bold"),
        width=10,
        height=1,
        bg="#c8a96e",
        fg="#1a1a2e",
        activebackground="#e8c98e",
        activeforeground="#1a1a2e",
        relief="solid",
        bd=2,
        cursor="hand2",
        command=credits_win.destroy,
    )
    close_button.pack(pady=(0, 20))


def _update_toolbar():
    """
       Update toolbar information including current step count,
       path history, clue count, and rewind availability.
       """
    _step_label.config(text=f"— Step {engine.step_counter}")

    if engine.can_rewind():
        _rewind_btn.config(state=NORMAL, fg="#1a1a2e")
    else:
        _rewind_btn.config(state=DISABLED, fg="#888888")

    path = engine.get_path_history()

    if path:
        display = " > ".join(path[-4:])
        if len(path) > 4:
            display = "... > " + display
    else:
        display = "—"

    _path_label.config(text=f"Path: {display}")
    _clue_count_label.config(text=f"Clues: {engine.clue_heap.size()}")

    if _evidence_window and _evidence_window.winfo_exists():
        _evidence_window.refresh()


def show_page(new_clue=False):
    """
      Refresh the current story scene and dynamically update
      GUI based on the active StoryNode.
      If a new clue is discovered, a temporary notification
      banner is displayed to the player.
      """
    clear_screen()
    hide_main_menu()

    toolbar.pack(fill=X, side=TOP)
    status_bar.pack(fill=X, side=BOTTOM)

    node = engine.get_current_node()

    if node.bg_image:
        set_background(node.bg_image)

    title_label.config(text=node.title)
    title_label.pack(pady=20)

    story_text.config(state=NORMAL)
    story_text.delete("1.0", END)
    story_text.insert(END, node.text)
    story_text.place(relx=0.5, rely=0.78, anchor=CENTER)
    story_text.config(state=DISABLED)

    if new_clue and node.clue:
        _clue_banner.config(
            text=f"  New clue found: {node.clue['name']}  "
                 f"(importance {node.clue['importance']}/10)"
        )
        _clue_banner.place(relx=0.5, rely=0.13, anchor=CENTER)
        #Make the "clue banner" automatically disappear after 3.5 seconds.
        root.after(3500, _clue_banner.place_forget)

    if node.is_ending:
        ending_frame.place(relx=0.5, rely=0.92, anchor=CENTER)

        analyze_button.config(command=_open_analysis)
        analyze_button.pack(side=LEFT, padx=15)

        restart_button.config(command=_on_restart)
        restart_button.pack(side=LEFT, padx=15)

        exit_button.config(command=root.destroy)
        exit_button.pack(side=LEFT, padx=15)

    elif len(node.choices) == 2:
        choice_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

        choice_button1.config(
            text=node.choices[0][0],
            command=lambda: _make_choice(0),
        )
        choice_button1.pack(side=TOP, pady=6)

        choice_button2.config(
            text=node.choices[1][0],
            command=lambda: _make_choice(1),
        )
        choice_button2.pack(side=TOP, pady=6)

    elif len(node.choices) == 1:
        if engine.step_counter == 0:
            btn_text = "Start"
        else:
            btn_text = "Next"

        main_button.config(text=btn_text, command=lambda: _make_choice(0))
        main_button.place(relx=0.5, rely=0.55, anchor=CENTER)

    menu_button.config(command=show_main_menu)
    menu_button.place(relx=0.92, rely=0.08, anchor=CENTER)

    _update_toolbar()


def _make_choice(index):
    prev_count = engine.clue_heap.size()

    if engine.make_choice(index):
        new_clue = engine.clue_heap.size() > prev_count
        show_page(new_clue=new_clue)


def _on_rewind():
    if engine.rewind():
        show_page()


def _on_restart():
    answer = messagebox.askyesno(
        "Restart",
        "Start the investigation from the beginning?\nAll progress will be lost.",
        parent=root,
    )

    if answer:
        engine.restart()
        show_page()


def _open_evidence():
    global _evidence_window

    if _evidence_window and _evidence_window.winfo_exists():
        _evidence_window.lift()
        _evidence_window.refresh()
    else:
        _evidence_window = EvidencePanel(root, engine)


def _open_analysis():
    global _analysis_window

    if _analysis_window and _analysis_window.winfo_exists():
        _analysis_window.win.lift()
    else:
        _analysis_window = AnalysisWindow(root, engine)


# =============================================================================
# SECTION 8 — ENTRY POINT
# =============================================================================

show_main_menu()
root.mainloop()