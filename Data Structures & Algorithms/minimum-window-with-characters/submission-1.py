from collections import defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Create frequency map for target string
        target_freq = defaultdict(int)
        for char in t:
            target_freq[char] += 1
        
        # Initialize sliding window variables
        positions = deque()  # Store positions of relevant characters
        window_freq = defaultdict(int)  # Character frequencies in current window
        min_len = float('inf')
        min_start = 0
        chars_matched = 0  # Count of character types that match required frequency
        required_chars = len(target_freq)
        
        # Process each character in s
        for i, char in enumerate(s):
            # Only process characters that are in target string
            if char in target_freq:
                # Add current position to deque
                positions.append(i)
                
                # Update window frequency
                window_freq[char] += 1
                
                # Check if this character's frequency now matches or exceeds required
                if window_freq[char] == target_freq[char]:
                    chars_matched += 1
            
            # If we have all required characters, try to shrink window
            while chars_matched == required_chars and positions:
                # Calculate current window length
                start_idx = positions[0]
                end_idx = i
                window_len = end_idx - start_idx + 1
                
                # Update minimum window if this one is smaller
                if window_len < min_len:
                    min_len = window_len
                    min_start = start_idx
                
                # Try to remove leftmost character
                left_char = s[positions[0]]
                positions.popleft()
                
                # Update frequency and matched count
                window_freq[left_char] -= 1
                if window_freq[left_char] < target_freq[left_char]:
                    chars_matched -= 1
        
        # If we found a valid window, return it
        if min_len != float('inf'):
            return s[min_start:min_start + min_len]
        else:
            return ""