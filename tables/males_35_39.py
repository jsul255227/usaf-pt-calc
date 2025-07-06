# males_35_39.py
# Official USAF PT scoring tables for Males 35-39
# Template based on males_under_25.py, males_25_29.py, and males_30_34.py. Fill in each component as official values are provided.

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
MALE_35_39_RUN = [
    # Official USAF PT 1.5 Mile Run scoring table for Males 35-39
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Lower time = higher score.
    # (0, mmss_to_seconds('9:45'), 60.0) means any time less than 9:45 earns 60.0 points.
    (0, mmss_to_seconds('9:45') - 1, 60.0),                 # < 9:45
    (mmss_to_seconds('9:45'), mmss_to_seconds('10:10'), 59.5),
    (mmss_to_seconds('10:11'), mmss_to_seconds('10:23'), 59.0),
    (mmss_to_seconds('10:24'), mmss_to_seconds('10:37'), 58.5),
    (mmss_to_seconds('10:38'), mmss_to_seconds('10:51'), 58.0),
    (mmss_to_seconds('10:52'), mmss_to_seconds('11:06'), 57.5),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 57.0),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 56.5),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 56.0),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 55.5),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 55.0),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 54.5),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 54.0),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 53.5),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 52.0),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 50.5),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 48.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 45.5),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 43.0),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 40.5),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 38.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 35.0), # 17:34*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Example: (101, float('inf'), 60.0) means 101 or more shuttles earns 60.0 points.
MALE_35_39_HAMR = [
    # Official USAF PT HAMR scoring table for Males 35-39
    # Each tuple: (start_shuttles, end_shuttles, score)
    # Ranges are inclusive. Higher shuttles = higher score.
    # (93, float('inf'), 60.0) means > 92 shuttles earns 60.0 points.
    (93, float('inf'), 60.0),         # > 92
    (87, 92, 59.5),
    (83, 86, 59.0),
    (80, 82, 58.5),
    (77, 79, 58.0),
    (74, 76, 57.5),
    (71, 73, 57.0),
    (68, 70, 56.5),
    (65, 67, 56.0),
    (62, 64, 55.5),
    (59, 61, 55.0),
    (56, 58, 54.5),
    (54, 55, 54.0),
    (51, 53, 53.5),
    (48, 50, 52.0),
    (45, 47, 50.5),
    (42, 44, 48.0),
    (39, 41, 45.5),
    (36, 38, 43.0),
    (33, 35, 40.5),
    (30, 32, 38.0),
    (27, 29, 35.0),                   # 27*-29
]

# ----------------------
# Upper Body: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (67, float('inf'), 20.0) means 67 or more push-ups earns 20.0 points.
MALE_35_39_PUSHUPS = [
    # Official USAF PT 1 min Push-ups scoring table for Males 35-39
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (52, float('inf'), 20.0) means > 51 push-ups earns 20.0 points.
    (52, float('inf'), 20.0),      # > 51
    (50, 51, 19.5),
    (49, 49, 19.0),
    (48, 48, 18.8),
    (47, 47, 18.6),
    (46, 46, 18.5),
    (45, 45, 18.4),
    (44, 44, 18.2),
    (43, 43, 18.0),
    (42, 42, 17.8),
    (41, 41, 17.6),
    (40, 40, 17.4),
    (39, 39, 17.2),
    (38, 38, 17.0),
    (37, 37, 16.6),
    (36, 36, 16.0),
    (35, 35, 15.6),
    (34, 34, 15.4),
    (33, 33, 15.0),
    (32, 32, 14.6),
    (31, 31, 14.0),
    (30, 30, 13.6),
    (29, 29, 13.4),
    (28, 28, 13.0),
    (27, 27, 12.0),
    (26, 26, 11.0),
    (25, 25, 10.6),
    (24, 24, 10.0),
    (23, 23, 7.0),
    (22, 22, 4.0),
    (21, 21, 1.0),                # 21*
]

# ----------------------
# Upper Body: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (41, float('inf'), 20.0) means 41 or more HR push-ups earns 20.0 points.
MALE_35_39_HR_PUSHUPS = [
    # Official USAF PT 2 min Hand Release Push-ups scoring table for Males 35-39
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (41, float('inf'), 20.0) means > 40 HR push-ups earns 20.0 points.
    (41, float('inf'), 20.0),      # > 40
    (39, 40, 19.6),
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
MALE_35_39_SITUPS = [
    # Official USAF PT 1 min Sit-ups scoring table for Males 35-39
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (53, float('inf'), 20.0) means > 52 sit-ups earns 20.0 points.
    (53, float('inf'), 20.0),      # > 52
    (51, 52, 19.7),
    (50, 50, 19.4),
    (49, 49, 19.0),
    (48, 48, 18.8),
    (47, 47, 18.4),
    (46, 46, 18.0),
    (45, 45, 17.6),
    (44, 44, 17.4),
    (43, 43, 17.0),
    (42, 42, 16.6),
    (41, 41, 16.0),
    (40, 40, 15.0),
    (39, 39, 14.0),
    (38, 38, 13.0),
    (37, 37, 12.0),
    (36, 36, 9.0),
    (35, 35, 6.0),
    (34, 34, 3.0),                # 34*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (50, float('inf'), 20.0) means 50 or more crunches earns 20.0 points.
MALE_35_39_CRUNCH = [
    # Official USAF PT 2 min Cross Leg Reverse Crunch scoring table for Males 35-39
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (47, float('inf'), 20.0) means > 46 crunches earns 20.0 points.
    (47, float('inf'), 20.0),      # > 46
    (45, 46, 19.6),
    (44, 44, 19.3),
    (43, 43, 18.9),
    (42, 42, 18.6),
    (41, 41, 18.2),
    (40, 40, 17.9),
    (39, 39, 17.5),
    (38, 38, 17.1),
    (37, 37, 16.8),
    (36, 36, 16.4),
    (35, 35, 16.1),
    (34, 34, 15.7),
    (33, 33, 15.4),
    (32, 32, 15.0),
    (31, 31, 14.6),
    (30, 30, 14.3),
    (29, 29, 13.9),
    (28, 28, 13.6),
    (27, 27, 13.2),
    (26, 26, 12.9),
    (25, 25, 12.5),
    (24, 24, 12.1),
    (23, 23, 11.8),
    (22, 22, 11.4),
    (21, 21, 11.1),
    (20, 20, 10.7),
    (19, 19, 10.4),
    (18, 18, 10.0),                # 18*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
# Example: (mmss_to_seconds('3:36'), float('inf'), 20.0) means any time above 3:35 earns 20.0 points.
MALE_35_39_PLANK = [
    # Official USAF PT Forearm Plank scoring table for Males 35-39
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Higher time = higher score.
    # (mmss_to_seconds('3:21'), float('inf'), 20.0) means any time above 3:20 earns 20.0 points.
    (mmss_to_seconds('3:21'), float('inf'), 20.0),   # > 3:20
    (mmss_to_seconds('3:15'), mmss_to_seconds('3:20'), 19.7),
    (mmss_to_seconds('3:10'), mmss_to_seconds('3:14'), 19.3),
    (mmss_to_seconds('3:04'), mmss_to_seconds('3:09'), 18.9),
    (mmss_to_seconds('2:57'), mmss_to_seconds('3:03'), 18.5),
    (mmss_to_seconds('2:50'), mmss_to_seconds('2:56'), 18.0),
    (mmss_to_seconds('2:30'), mmss_to_seconds('2:49'), 16.7),
    (mmss_to_seconds('2:10'), mmss_to_seconds('2:29'), 15.3),
    (mmss_to_seconds('1:50'), mmss_to_seconds('2:09'), 14.0),
    (mmss_to_seconds('1:30'), mmss_to_seconds('1:49'), 12.7),
    (mmss_to_seconds('1:10'), mmss_to_seconds('1:29'), 11.3),
    (mmss_to_seconds('0:50'), mmss_to_seconds('1:09'), 10.0),   # 0:50* minimum
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
# * Minimum Component Values (Males 35-39):
#   - Run time < [FILL IN]
#   - 20 m HAMR Shuttles > [FILL IN]
#
# Composite Score Categories:
#   - Excellent:     ≥ 90.0 pts
#   - Satisfactory:  75.0 - 89.9
#   - Unsatisfactory: < 75.0
#
# These notes apply to all scoring tables and should be referenced in calculator logic and UI.
