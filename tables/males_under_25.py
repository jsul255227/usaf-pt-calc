# males_under_25.py
# Official USAF PT scoring tables for Males Under 25
# Each table is a list of (start, end, score) tuples for a specific component.
# Use mmss_to_seconds for time-based events (e.g., run, plank).
# All values and ranges are based on the official USAF tables.

# Helper function: Convert 'mm:ss' string to total seconds (int)
def mmss_to_seconds(mmss):
    """
    Convert a time string in 'mm:ss' format to total seconds.
    Example: '9:13' -> 553
    """
    m, s = map(int, mmss.split(':'))
    return m * 60 + s

# ----------------------
# Cardio: 1.5 Mile Run
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
# Example: (0, mmss_to_seconds('9:12'), 60.0) means any time from 0 up to 9:12 earns 60.0 points.
MALE_UNDER_25_RUN = [
    (0, mmss_to_seconds('9:12'), 60.0),
    (mmss_to_seconds('9:13'), mmss_to_seconds('9:34'), 59.5),
    (mmss_to_seconds('9:35'), mmss_to_seconds('9:45'), 59.0),
    (mmss_to_seconds('9:46'), mmss_to_seconds('9:58'), 58.5),
    (mmss_to_seconds('9:59'), mmss_to_seconds('10:10'), 58.0),
    (mmss_to_seconds('10:11'), mmss_to_seconds('10:23'), 57.5),
    (mmss_to_seconds('10:24'), mmss_to_seconds('10:37'), 57.0),
    (mmss_to_seconds('10:38'), mmss_to_seconds('10:51'), 56.5),
    (mmss_to_seconds('10:52'), mmss_to_seconds('11:06'), 56.0),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 55.5),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 55.0),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 54.5),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 54.0),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 53.5),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 52.0),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 50.5),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 49.0),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 46.5),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 44.0),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 41.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 38.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 35.0),
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Example: (101, float('inf'), 60.0) means 101 or more shuttles earns 60.0 points.
MALE_UNDER_25_HAMR = [
    (101, float('inf'), 60.0),      # > 100
    (94, 99, 59.5),
    (92, 93, 59.0),
    (88, 91, 58.5),
    (86, 87, 58.0),
    (83, 85, 57.5),
    (80, 82, 57.0),
    (77, 79, 56.5),
    (74, 76, 56.0),
    (71, 73, 55.5),
    (68, 70, 55.0),
    (65, 67, 54.5),
    (62, 64, 54.0),
    (59, 61, 53.5),
    (56, 58, 52.0),
    (54, 55, 50.5),
    (51, 53, 49.0),
    (48, 50, 46.5),
    (45, 47, 44.0),
    (42, 44, 41.0),
    (39, 41, 38.0),
    (36, 38, 35.0),                # 36*-38
]

# ----------------------
# Upper Body: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (67, float('inf'), 20.0) means 67 or more push-ups earns 20.0 points.
MALE_UNDER_25_PUSHUPS = [
    (67, float('inf'), 20.0),      # ≥ 67
    (66, 66, 19.8),
    (65, 65, 19.6),
    (64, 64, 19.4),
    (63, 63, 19.2),
    (62, 62, 19.0),
    (61, 61, 18.8),
    (60, 60, 18.6),
    (59, 59, 18.4),
    (58, 58, 18.2),
    (57, 57, 18.0),
    (56, 56, 17.8),
    (55, 55, 17.7),
    (54, 54, 17.6),
    (53, 53, 17.4),
    (52, 52, 17.2),
    (51, 51, 17.0),
    (50, 50, 16.8),
    (49, 49, 16.6),
    (48, 48, 16.2),
    (47, 47, 16.0),
    (46, 46, 15.6),
    (45, 45, 15.4),
    (44, 44, 15.0),
    (43, 43, 14.6),
    (42, 42, 14.4),
    (41, 41, 14.0),
    (40, 40, 13.6),
    (39, 39, 13.0),
    (38, 38, 12.6),
    (37, 37, 12.0),
    (36, 36, 11.6),
    (35, 35, 11.0),
    (34, 34, 10.6),
    (33, 33, 10.0),
    (32, 32, 7.0),
    (31, 31, 4.0),
    (30, 30, 1.0),                # 30*
]

# ----------------------
# Upper Body: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (41, float('inf'), 20.0) means 41 or more HR push-ups earns 20.0 points.
MALE_UNDER_25_HR_PUSHUPS = [
    (41, float('inf'), 20.0),      # > 40
    (39, 39, 19.6),
    (38, 38, 19.2),
    (37, 37, 18.8),
    (36, 36, 18.4),
    (35, 35, 18.0),
    (34, 34, 17.6),
    (33, 33, 17.2),
    (32, 32, 16.8),
    (31, 31, 16.4),
    (30, 30, 16.0),
    (29, 29, 15.6),
    (28, 28, 15.2),
    (27, 27, 14.8),
    (26, 26, 14.4),
    (25, 25, 14.0),
    (24, 24, 13.6),
    (23, 23, 13.2),
    (22, 22, 12.8),
    (21, 21, 12.4),
    (20, 20, 12.0),
    (19, 19, 11.6),
    (18, 18, 11.2),
    (17, 17, 10.8),
    (16, 16, 10.4),
    (15, 15, 10.0),                # 15*
]

# ----------------------
# Core: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (58, float('inf'), 20.0) means 58 or more sit-ups earns 20.0 points.
MALE_UNDER_25_SITUPS = [
    (58, float('inf'), 20.0),      # ≥ 58
    (57, 57, 19.7),
    (56, 56, 19.4),
    (55, 55, 19.0),
    (54, 54, 18.8),
    (53, 53, 18.4),
    (52, 52, 18.0),
    (51, 51, 17.6),
    (50, 50, 17.4),
    (49, 49, 17.0),
    (48, 48, 16.6),
    (47, 47, 16.0),
    (46, 46, 15.0),
    (45, 45, 14.0),
    (44, 44, 13.0),
    (43, 43, 12.6),
    (42, 42, 12.0),
    (41, 41, 9.0),
    (40, 40, 6.0),
    (39, 39, 3.0),                # 39*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (50, float('inf'), 20.0) means 50 or more crunches earns 20.0 points.
MALE_UNDER_25_CRUNCH = [
    (50, float('inf'), 20.0),      # > 49
    (48, 48, 19.6),
    (47, 47, 19.3),
    (46, 46, 18.9),
    (45, 45, 18.6),
    (44, 44, 18.2),
    (43, 43, 17.9),
    (42, 42, 17.5),
    (41, 41, 17.1),
    (40, 40, 16.8),
    (39, 39, 16.4),
    (38, 38, 16.1),
    (37, 37, 15.7),
    (36, 36, 15.4),
    (35, 35, 15.0),
    (34, 34, 14.6),
    (33, 33, 14.3),
    (32, 32, 13.9),
    (31, 31, 13.6),
    (30, 30, 13.2),
    (29, 29, 12.9),
    (28, 28, 12.5),
    (27, 27, 12.1),
    (26, 26, 11.8),
    (25, 25, 11.4),
    (24, 24, 11.1),
    (23, 23, 10.7),
    (22, 22, 10.4),
    (21, 21, 10.0),                # 21*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
# Example: (mmss_to_seconds('3:36'), float('inf'), 20.0) means any time above 3:35 earns 20.0 points.
MALE_UNDER_25_PLANK = [
    (mmss_to_seconds('3:36'), float('inf'), 20.0),      # > 3:35
    (mmss_to_seconds('3:30'), mmss_to_seconds('3:35'), 19.7),
    (mmss_to_seconds('3:25'), mmss_to_seconds('3:29'), 19.3),
    (mmss_to_seconds('3:18'), mmss_to_seconds('3:24'), 18.9),
    (mmss_to_seconds('3:12'), mmss_to_seconds('3:17'), 18.5),
    (mmss_to_seconds('3:05'), mmss_to_seconds('3:11'), 18.0),
    (mmss_to_seconds('2:45'), mmss_to_seconds('3:04'), 16.7),
    (mmss_to_seconds('2:25'), mmss_to_seconds('2:44'), 15.3),
    (mmss_to_seconds('2:05'), mmss_to_seconds('2:24'), 14.0),
    (mmss_to_seconds('1:55'), mmss_to_seconds('2:04'), 13.3),
    (mmss_to_seconds('1:25'), mmss_to_seconds('1:54'), 11.3),
    (mmss_to_seconds('1:05'), mmss_to_seconds('1:24'), 10.0), # 1:05*
]

# ----------------------
# USAF PT Test: Scoring Notes and Composite Categories
# ----------------------
# Health Risk Category:
#   - low, moderate or high risk for: current and future cardiovascular disease, diabetes, certain cancers, and other health problems.
#
# Passing Requirements:
#   1) Achieve a composite point total ≥ 75 points
#   2) Meet minimum point values for all components
#
# * Minimum Component Values (Males Under 25):
#   - Run time < 15:50
#   - 20 m HAMR Shuttles > 36 Shuttles
#
# Composite Score Categories:
#   - Excellent:     ≥ 90.0 pts
#   - Satisfactory:  75.0 - 89.9
#   - Unsatisfactory: < 75.0
#
# These notes apply to all scoring tables and should be referenced in calculator logic and UI.
