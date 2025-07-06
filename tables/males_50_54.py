# males_50_54.py
# Official USAF PT scoring tables for Males 50-54
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
MALE_50_54_RUN = [
    # Official USAF PT 1.5 Mile Run scoring table for Males 50-54
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Lower time = higher score.
    # (0, mmss_to_seconds('10:37'), 60.0) means any time less than 10:37 earns 60.0 points.
    (0, mmss_to_seconds('10:37') - 1, 60.0),                 # < 10:37
    (mmss_to_seconds('10:37'), mmss_to_seconds('11:06'), 59.5),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 59.0),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 58.5),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 58.0),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 57.5),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 57.0),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 56.5),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 56.0),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 55.5),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 55.0),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 54.5),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 54.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 53.5),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 52.0),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 50.5),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 48.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 45.5),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 43.0),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 40.5),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 38.0),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 35.0), # 20:33*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
MALE_50_54_HAMR = [
    # Official USAF PT HAMR scoring table for Males 50-54
    # Each tuple: (start_shuttles, end_shuttles, score)
    # Ranges are inclusive. Higher shuttles = higher score.
    # (81, float('inf'), 60.0) means > 80 shuttles earns 60.0 points.
    (81, float('inf'), 60.0),         # > 80
    (74, 80, 59.5),
    (71, 73, 59.0),
    (68, 70, 58.5),
    (65, 67, 58.0),
    (62, 64, 57.5),
    (59, 61, 57.0),
    (56, 58, 56.5),
    (54, 55, 56.0),
    (51, 53, 55.5),
    (48, 50, 55.0),
    (45, 47, 54.5),
    (42, 44, 54.0),
    (39, 41, 53.5),
    (36, 38, 52.0),
    (33, 35, 50.5),
    (30, 32, 48.0),
    (27, 29, 45.5),
    (24, 26, 43.0),
    (22, 23, 40.5),
    (19, 21, 38.0),
    (16, 18, 35.0),                   # 16*-18
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
MALE_50_54_PLANK = [
    # Official USAF PT Forearm Plank scoring table for Males 50-54
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Higher time = higher score.
    # (mmss_to_seconds('3:06'), float('inf'), 20.0) means any time above 3:05 earns 20.0 points.
    (mmss_to_seconds('3:06'), float('inf'), 20.0),   # > 3:05
    (mmss_to_seconds('3:00'), mmss_to_seconds('3:05'), 19.7),
    (mmss_to_seconds('2:55'), mmss_to_seconds('2:59'), 19.3),
    (mmss_to_seconds('2:49'), mmss_to_seconds('2:54'), 18.9),
    (mmss_to_seconds('2:42'), mmss_to_seconds('2:48'), 18.5),
    (mmss_to_seconds('2:35'), mmss_to_seconds('2:41'), 18.0),
    (mmss_to_seconds('2:15'), mmss_to_seconds('2:34'), 16.7),
    (mmss_to_seconds('1:55'), mmss_to_seconds('2:14'), 15.3),
    (mmss_to_seconds('1:35'), mmss_to_seconds('1:54'), 14.0),
    (mmss_to_seconds('1:15'), mmss_to_seconds('1:34'), 12.7),
    (mmss_to_seconds('0:55'), mmss_to_seconds('1:14'), 11.3),
    (mmss_to_seconds('0:35'), mmss_to_seconds('0:54'), 10.0),   # 0:35* minimum
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
MALE_50_54_PUSHUPS = [
    # Official USAF PT 1 min Push-ups scoring table for Males 50-54
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (37, float('inf'), 20.0) means > 36 push-ups earns 20.0 points.
    (37, float('inf'), 20.0),      # > 36
    (35, 36, 19.7),
    (34, 34, 19.4),
    (33, 33, 19.0),
    (32, 32, 18.8),
    (31, 31, 18.4),
    (30, 30, 18.2),
    (29, 29, 18.0),
    (28, 28, 17.6),
    (27, 27, 17.4),
    (26, 26, 17.0),
    (25, 25, 16.6),
    (24, 24, 16.0),
    (23, 23, 15.0),
    (22, 22, 14.0),
    (21, 21, 13.0),
    (20, 20, 12.6),
    (19, 19, 12.0),
    (18, 18, 11.6),
    (17, 17, 11.0),
    (16, 16, 10.6),
    (15, 15, 10.0),
    (14, 14, 7.0),
    (13, 13, 4.0),
    (12, 12, 1.0),                # 12*
]

# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
MALE_50_54_HR_PUSHUPS = [
    # Official USAF PT 2 min Hand Release Push-ups scoring table for Males 50-54
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (36, float('inf'), 20.0) means > 35 HR push-ups earns 20.0 points.
    (36, float('inf'), 20.0),      # > 35
    (34, 35, 19.6),
    (33, 33, 19.2),
    (32, 32, 18.8),
    (31, 31, 18.3),
    (30, 30, 17.9),
    (29, 29, 17.5),
    (28, 28, 17.1),
    (27, 27, 16.7),
    (26, 26, 16.3),
    (25, 25, 15.8),
    (24, 24, 15.4),
    (23, 23, 15.0),
    (22, 22, 14.6),
    (21, 21, 14.2),
    (20, 20, 13.8),
    (19, 19, 13.3),
    (18, 18, 12.9),
    (17, 17, 12.5),
    (16, 16, 12.1),
    (15, 15, 11.7),
    (14, 14, 11.3),
    (13, 13, 10.8),
    (12, 12, 10.4),
    (11, 11, 10.0),                # 11*
]

# ----------------------
# Strength: 2 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
MALE_50_54_SITUPS = [
    # Official USAF PT 1 min Sit-ups scoring table for Males 50-54
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    # (47, float('inf'), 20.0) means > 46 sit-ups earns 20.0 points.
    (47, float('inf'), 20.0),      # > 46
    (45, 46, 19.7),
    (44, 44, 19.4),
    (43, 43, 19.0),
    (42, 42, 18.8),
    (41, 41, 18.4),
    (40, 40, 18.2),
    (39, 39, 18.0),
    (38, 38, 17.6),
    (37, 37, 17.4),
    (36, 36, 17.0),
    (35, 35, 16.0),
    (34, 34, 15.6),
    (33, 33, 15.0),
    (32, 32, 14.6),
    (31, 31, 14.0),
    (30, 30, 13.0),
    (29, 29, 12.6),
    (28, 28, 12.0),
    (27, 27, 9.0),
    (26, 26, 6.0),
    (25, 25, 3.0),                # 25*
]

# ----------------------
# Core: Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
MALE_50_54_CRUNCH = [
    # Official USAF PT 2 min Cross Leg Reverse Crunch scoring table for Males 50-54
    # Each tuple: (start_reps, end_reps, score)
    # Ranges are inclusive. Higher reps = higher score.
    (43, float('inf'), 20.0),      # > 42
    (41, 42, 19.7),
    (40, 40, 19.4),
    (39, 39, 19.1),
    (38, 38, 18.8),
    (37, 37, 18.5),
    (36, 36, 18.2),
    (35, 35, 17.9),
    (34, 34, 17.6),
    (33, 33, 17.3),
    (32, 32, 17.0),
    (31, 31, 16.7),
    (30, 30, 16.4),
    (29, 29, 16.1),
    (28, 28, 15.8),
    (27, 27, 15.5),
    (26, 26, 15.2),
    (25, 25, 14.8),
    (24, 24, 14.5),
    (23, 23, 14.2),
    (22, 22, 13.9),
    (21, 21, 13.6),
    (20, 20, 13.3),
    (19, 19, 13.0),
    (18, 18, 12.7),
    (17, 17, 12.4),
    (16, 16, 12.1),
    (15, 15, 11.8),
    (14, 14, 11.5),
    (13, 13, 11.2),
    (12, 12, 10.9),
    (11, 11, 10.6),
    (10, 10, 10.3),
    (9, 9, 10.0),                # 9*
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
# * Minimum Component Values (Males 50-54):
#   - Run time < [FILL IN]
#   - 20 m HAMR Shuttles > [FILL IN]
#
# Composite Score Categories:
#   - Excellent:     ≥ 90.0 pts
#   - Satisfactory:  75.0 - 89.9
#   - Unsatisfactory: < 75.0
#
# These notes apply to all scoring tables and should be referenced in calculator logic and UI.
