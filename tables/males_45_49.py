# males_45_49.py
# Official USAF PT scoring tables for Males 45-49
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
MALE_45_49_RUN = [
    # Official USAF PT 1.5 Mile Run scoring table for Males 45-49
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Lower time = higher score.
    # (0, mmss_to_seconds('10:10'), 60.0) means any time less than 10:10 earns 60.0 points.
    (0, mmss_to_seconds('10:10') - 1, 60.0),                 # < 10:10
    (mmss_to_seconds('10:10'), mmss_to_seconds('10:37'), 59.5),
    (mmss_to_seconds('10:38'), mmss_to_seconds('10:51'), 59.0),
    (mmss_to_seconds('10:52'), mmss_to_seconds('11:06'), 58.5),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 58.0),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 57.5),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 57.0),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 56.5),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 56.0),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 55.5),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 55.0),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 54.5),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 54.0),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 53.5),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 52.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 50.5),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 49.0),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 46.5),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 44.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 41.0),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 38.0),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 35.0), # 18:56*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Example: (101, float('inf'), 60.0) means > 100 shuttles earns 60.0 points.
MALE_45_49_HAMR = [
    # Official USAF PT HAMR scoring table for Males 45-49
    # Each tuple: (start_shuttles, end_shuttles, score)
    # Ranges are inclusive. Higher shuttles = higher score.
    # (87, float('inf'), 60.0) means > 86 shuttles earns 60.0 points.
    (87, float('inf'), 60.0),         # > 86
    (80, 86, 59.5),
    (77, 79, 59.0),
    (74, 76, 58.5),
    (71, 73, 58.0),
    (68, 70, 57.5),
    (65, 67, 57.0),
    (62, 64, 56.5),
    (59, 61, 56.0),
    (56, 58, 55.5),
    (54, 55, 55.0),
    (51, 53, 54.5),
    (48, 50, 54.0),
    (45, 47, 53.5),
    (42, 44, 52.0),
    (39, 41, 50.5),
    (36, 38, 49.0),
    (33, 35, 46.5),
    (30, 32, 44.0),
    (27, 29, 41.0),
    (24, 26, 38.0),
    (22, 23, 35.0),                   # 22*-23
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
MALE_45_49_PLANK = [
    # Official USAF PT Forearm Plank scoring table for Males 45-49
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Higher time = higher score.
    # (mmss_to_seconds('3:11'), float('inf'), 20.0) means any time above 3:10 earns 20.0 points.
    (mmss_to_seconds('3:11'), float('inf'), 20.0),   # > 3:10
    (mmss_to_seconds('3:05'), mmss_to_seconds('3:10'), 19.7),
    (mmss_to_seconds('3:00'), mmss_to_seconds('3:04'), 19.3),
    (mmss_to_seconds('2:54'), mmss_to_seconds('2:59'), 18.9),
    (mmss_to_seconds('2:47'), mmss_to_seconds('2:53'), 18.5),
    (mmss_to_seconds('2:40'), mmss_to_seconds('2:46'), 18.0),
    (mmss_to_seconds('2:20'), mmss_to_seconds('2:39'), 16.7),
    (mmss_to_seconds('2:00'), mmss_to_seconds('2:19'), 15.3),
    (mmss_to_seconds('1:40'), mmss_to_seconds('1:59'), 14.0),
    (mmss_to_seconds('1:20'), mmss_to_seconds('1:39'), 12.7),
    (mmss_to_seconds('1:00'), mmss_to_seconds('1:19'), 11.3),
    (mmss_to_seconds('0:40'), mmss_to_seconds('0:59'), 10.0),   # 0:40* minimum
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
MALE_45_49_PUSHUPS = [
    # Official USAF PT 1 min Push-ups scoring table for Males 45-49
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (45, float('inf'), 20.0) means > 44 push-ups earns 20.0 points.
    (45, float('inf'), 20.0),      # > 44
    (43, 44, 19.8),
    (42, 42, 19.6),
    (41, 41, 19.4),
    (40, 40, 19.2),
    (39, 39, 19.0),
    (38, 38, 18.8),
    (37, 37, 18.4),
    (36, 36, 18.2),
    (35, 35, 18.0),
    (34, 34, 17.6),
    (33, 33, 17.0),
    (32, 32, 16.8),
    (31, 31, 16.6),
    (30, 30, 16.2),
    (29, 29, 16.0),
    (28, 28, 15.0),
    (27, 27, 14.6),
    (26, 26, 14.4),
    (25, 25, 14.0),
    (24, 24, 13.0),
    (23, 23, 12.6),
    (22, 22, 12.0),
    (21, 21, 11.6),
    (20, 20, 11.0),
    (19, 19, 10.6),
    (18, 18, 10.0),
    (17, 17, 7.0),
    (16, 16, 4.0),
    (15, 15, 1.0),                # 15*
]

# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
MALE_45_49_HR_PUSHUPS = [
    # Official USAF PT 2 min Hand Release Push-ups scoring table for Males 45-49
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
MALE_45_49_SITUPS = [
    # Official USAF PT 1 min Sit-ups scoring table for Males 45-49
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (49, float('inf'), 20.0) means > 48 sit-ups earns 20.0 points.
    (49, float('inf'), 20.0),      # > 48
    (47, 48, 19.7),
    (46, 46, 19.4),
    (45, 45, 19.2),
    (44, 44, 19.0),
    (43, 43, 18.8),
    (42, 42, 18.4),
    (41, 41, 18.0),
    (40, 40, 17.6),
    (39, 39, 17.4),
    (38, 38, 17.0),
    (37, 37, 16.6),
    (36, 36, 16.0),
    (35, 35, 15.6),
    (34, 34, 15.0),
    (33, 33, 14.0),
    (32, 32, 13.0),
    (31, 31, 12.0),
    (30, 30, 9.0),
    (29, 29, 6.0),
    (28, 28, 3.0),                # 28*
]

# ----------------------
# Core: Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
MALE_45_49_CRUNCH = [
    # Official USAF PT 2 min Cross Leg Reverse Crunch scoring table for Males 45-49
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    (43, 43, 20.0),
    (42, 42, 19.7),
    (41, 41, 19.4),
    (40, 40, 19.1),
    (39, 39, 18.8),
    (38, 38, 18.4),
    (37, 37, 18.1),
    (36, 36, 17.8),
    (35, 35, 17.5),
    (34, 34, 17.2),
    (33, 33, 16.9),
    (32, 32, 16.6),
    (31, 31, 16.3),
    (30, 30, 15.9),
    (29, 29, 15.6),
    (28, 28, 15.3),
    (27, 27, 15.0),
    (26, 26, 14.7),
    (25, 25, 14.4),
    (24, 24, 14.1),
    (23, 23, 13.8),
    (22, 22, 13.4),
    (21, 21, 13.1),
    (20, 20, 12.8),
    (19, 19, 12.5),
    (18, 18, 12.2),
    (17, 17, 11.9),
    (16, 16, 11.6),
    (15, 15, 11.3),
    (14, 14, 10.9),
    (13, 13, 10.6),
    (12, 12, 10.3),
    (11, 11, 10.0),                # 11*
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
# * Minimum Component Values (Males 45-49):
#   - Run time < [FILL IN]
#   - 20 m HAMR Shuttles > [FILL IN]
#
# Composite Score Categories:
#   - Excellent:     ≥ 90.0 pts
#   - Satisfactory:  75.0 - 89.9
#   - Unsatisfactory: < 75.0
#
# These notes apply to all scoring tables and should be referenced in calculator logic and UI.
