# males_40_44.py
# Official USAF PT scoring tables for Males 40-44
# Template based on previous age groups. Fill in each component as official values are provided.

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
MALE_40_44_RUN = [
    # Official USAF PT 1.5 Mile Run scoring table for Males 40-44
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Lower time = higher score.
    # (0, mmss_to_seconds('9:58'), 60.0) means any time less than 9:58 earns 60.0 points.
    (0, mmss_to_seconds('9:58') - 1, 60.0),                 # < 9:58
    (mmss_to_seconds('9:58'), mmss_to_seconds('10:23'), 59.5),
    (mmss_to_seconds('10:24'), mmss_to_seconds('10:37'), 59.0),
    (mmss_to_seconds('10:38'), mmss_to_seconds('10:51'), 58.5),
    (mmss_to_seconds('10:52'), mmss_to_seconds('11:06'), 58.0),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 57.5),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 57.0),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 56.5),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 56.0),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 55.5),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 55.0),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 54.5),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 54.0),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 53.5),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 52.0),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 50.5),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 49.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 46.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 44.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 41.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 38.0),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 35.0), # 18:14*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Example: (101, float('inf'), 60.0) means 
MALE_40_44_HAMR = [
    # Official USAF PT HAMR scoring table for Males 40-44
    # Each tuple: (start_shuttles, end_shuttles, score)
    # Ranges are inclusive. Higher shuttles = higher score.
    # (89, float('inf'), 60.0) means > 88 shuttles earns 60.0 points.
    (89, float('inf'), 60.0),         # > 88
    (83, 88, 59.5),
    (80, 82, 59.0),
    (77, 79, 58.5),
    (74, 76, 58.0),
    (71, 73, 57.5),
    (68, 70, 57.0),
    (65, 67, 56.5),
    (62, 64, 56.0),
    (59, 61, 55.5),
    (56, 58, 55.0),
    (54, 55, 54.5),
    (51, 53, 54.0),
    (48, 50, 53.5),
    (45, 47, 52.0),
    (42, 44, 50.5),
    (39, 41, 49.0),
    (36, 38, 46.5),
    (33, 35, 44.0),
    (30, 32, 41.0),
    (27, 29, 38.0),
    (24, 26, 35.0),                   # 24*-26
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
# Example: (mmss_to_seconds('3:36'), float('inf'), 20.0) means any time above 3:35 earns 20.0 points.
MALE_40_44_PLANK = [
    # Official USAF PT Forearm Plank scoring table for Males 40-44
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Higher time = higher score.
    # (mmss_to_seconds('3:16'), float('inf'), 20.0) means any time above 3:15 earns 20.0 points.
    (mmss_to_seconds('3:16'), float('inf'), 20.0),   # > 3:15
    (mmss_to_seconds('3:10'), mmss_to_seconds('3:15'), 19.7),
    (mmss_to_seconds('3:05'), mmss_to_seconds('3:09'), 19.3),
    (mmss_to_seconds('2:59'), mmss_to_seconds('3:04'), 18.9),
    (mmss_to_seconds('2:52'), mmss_to_seconds('2:58'), 18.5),
    (mmss_to_seconds('2:45'), mmss_to_seconds('2:51'), 18.0),
    (mmss_to_seconds('2:25'), mmss_to_seconds('2:44'), 16.7),
    (mmss_to_seconds('2:05'), mmss_to_seconds('2:24'), 15.3),
    (mmss_to_seconds('1:45'), mmss_to_seconds('2:04'), 14.0),
    (mmss_to_seconds('1:25'), mmss_to_seconds('1:44'), 12.7),
    (mmss_to_seconds('1:05'), mmss_to_seconds('1:24'), 11.3),
    (mmss_to_seconds('0:45'), mmss_to_seconds('1:04'), 10.0),   # 0:45* minimum
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (45, float('inf'), 20.0) means > 44 push-ups earns 20.0 points.
MALE_40_44_PUSHUPS = [
    # Official USAF PT 1 min Push-ups scoring table for Males 40-44
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (45, float('inf'), 20.0) means > 44 push-ups earns 20.0 points.
    (45, float('inf'), 20.0),      # > 44
    (43, 44, 19.7),
    (42, 42, 19.4),
    (41, 41, 19.2),
    (40, 40, 19.0),
    (39, 39, 18.8),
    (38, 38, 18.4),
    (37, 37, 18.2),
    (36, 36, 18.0),
    (35, 35, 17.6),
    (34, 34, 17.0),
    (33, 33, 16.8),
    (32, 32, 16.6),
    (31, 31, 16.2),
    (30, 30, 16.0),
    (29, 29, 15.0),
    (28, 28, 14.6),
    (27, 27, 14.4),
    (26, 26, 14.0),
    (25, 25, 13.0),
    (24, 24, 12.0),
    (23, 23, 11.6),
    (22, 22, 11.0),
    (21, 21, 10.0),
    (20, 20, 7.0),
    (19, 19, 4.0),
    (18, 18, 1.0),                # 18*
]

# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (39, float('inf'), 20.0) means > 38 HR push-ups earns 20.0 points.
MALE_40_44_HR_PUSHUPS = [
    # Official USAF PT 2 min Hand Release Push-ups scoring table for Males 40-44
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (39, float('inf'), 20.0) means > 38 HR push-ups earns 20.0 points.
    (39, float('inf'), 20.0),      # > 38
    (37, 38, 19.6),
    (36, 36, 19.2),
    (35, 35, 18.8),
    (34, 34, 18.4),
    (33, 33, 18.0),
    (32, 32, 17.6),
    (31, 31, 17.2),
    (30, 30, 16.8),
    (29, 29, 16.4),
    (28, 28, 16.0),
    (27, 27, 15.6),
    (26, 26, 15.2),
    (25, 25, 14.8),
    (24, 24, 14.4),
    (23, 23, 14.0),
    (22, 22, 13.6),
    (21, 21, 13.2),
    (20, 20, 12.8),
    (19, 19, 12.4),
    (18, 18, 12.0),
    (17, 17, 11.6),
    (16, 16, 11.2),
    (15, 15, 10.8),
    (14, 14, 10.4),
    (13, 13, 10.0),                # 13*
]

# ----------------------
# Strength: 2 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (51, float('inf'), 20.0) means > 50 sit-ups earns 20.0 points.
MALE_40_44_SITUPS = [
    # Official USAF PT 1 min Sit-ups scoring table for Males 40-44
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (51, float('inf'), 20.0) means > 50 sit-ups earns 20.0 points.
    (51, float('inf'), 20.0),      # > 50
    (49, 50, 19.7),
    (48, 48, 19.4),
    (47, 47, 19.0),
    (46, 46, 18.8),
    (45, 45, 18.4),
    (44, 44, 18.2),
    (43, 43, 18.0),
    (42, 42, 17.6),
    (41, 41, 17.4),
    (40, 40, 17.0),
    (39, 39, 16.0),
    (38, 38, 15.6),
    (37, 37, 15.0),
    (36, 36, 14.0),
    (35, 35, 13.0),
    (34, 34, 12.0),
    (33, 33, 9.0),
    (32, 32, 6.0),
    (31, 31, 3.0),                # 31*
]

# ----------------------
# Core: Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (45, float('inf'), 20.0) means > 44 crunches earns 20.0 points.
MALE_40_44_CRUNCH = [
    # Official USAF PT 2 min Cross Leg Reverse Crunch scoring table for Males 40-44
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (45, float('inf'), 20.0) means > 44 crunches earns 20.0 points.
    (45, float('inf'), 20.0),      # > 44
    (43, 44, 19.6),
    (42, 42, 19.3),
    (41, 41, 18.9),
    (40, 40, 18.6),
    (39, 39, 18.2),
    (38, 38, 17.9),
    (37, 37, 17.5),
    (36, 36, 17.1),
    (35, 35, 16.8),
    (34, 34, 16.4),
    (33, 33, 16.1),
    (32, 32, 15.7),
    (31, 31, 15.4),
    (30, 30, 15.0),
    (29, 29, 14.6),
    (28, 28, 14.3),
    (27, 27, 13.9),
    (26, 26, 13.6),
    (25, 25, 13.2),
    (24, 24, 12.9),
    (23, 23, 12.5),
    (22, 22, 12.1),
    (21, 21, 11.8),
    (20, 20, 11.4),
    (19, 19, 11.1),
    (18, 18, 10.7),
    (17, 17, 10.4),
    (16, 16, 10.0),                # 16*
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
# * Minimum Component Values (Males 40-44):
#   - Run time < [FILL IN]
#   - 20 m HAMR Shuttles > [FILL IN]
#
# Composite Score Categories:
#   - Excellent:     ≥ 90.0 pts
#   - Satisfactory:  75.0 - 89.9
#   - Unsatisfactory: < 75.0
#
# These notes apply to all scoring tables and should be referenced in calculator logic and UI.
