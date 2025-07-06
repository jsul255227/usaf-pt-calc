# females_under_25.py
# Official USAF PT scoring tables for Females Under 25
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
# Cardio: 1.5 Mile Run (official July 2025)
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
# Updated to match official USAF PT table (July 2025)
FEMALE_UNDER_25_RUN = [
    (0, mmss_to_seconds('10:23') - 1, 60.0),                 # < 10:23
    (mmss_to_seconds('10:23'), mmss_to_seconds('10:51'), 59.5),
    (mmss_to_seconds('10:52'), mmss_to_seconds('11:06'), 59.0),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 58.5),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 58.0),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 57.5),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 57.0),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 56.5),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 56.0),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 55.5),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 55.0),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 54.5),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 54.0),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 53.5),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 52.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 50.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 49.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 46.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 42.5),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 39.0),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 35.0), # 18:56*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Updated to match official USAF PT table (July 2025)
FEMALE_UNDER_25_HAMR = [
    (84, float('inf'), 60.0),         # > 83
    (77, 82, 59.5),
    (74, 76, 59.0),
    (71, 73, 58.5),
    (68, 70, 58.0),
    (65, 67, 57.5),
    (62, 64, 57.0),
    (59, 61, 56.5),
    (56, 58, 56.0),
    (54, 55, 55.5),
    (51, 53, 55.0),
    (48, 50, 54.5),
    (45, 47, 54.0),
    (42, 44, 53.5),
    (39, 41, 52.0),
    (36, 38, 50.5),
    (33, 35, 49.0),
    (30, 32, 46.0),
    (27, 29, 42.5),
    (24, 26, 39.0),
    (22, 23, 35.0),                   # 22*-23
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
FEMALE_UNDER_25_PUSHUPS = [
    (48, float('inf'), 20.0),      # > 47
    (46, 47, 19.8),
    (45, 45, 19.6),
    (44, 44, 19.4),
    (43, 43, 19.2),
    (42, 42, 19.0),
    (41, 41, 18.8),
    (40, 40, 18.6),
    (39, 39, 18.4),
    (38, 38, 18.2),
    (37, 37, 18.0),
    (36, 36, 17.8),
    (35, 35, 17.6),
    (34, 34, 17.2),
    (33, 33, 17.0),
    (32, 32, 16.8),
    (31, 31, 16.6),
    (30, 30, 16.4),
    (29, 29, 16.2),
    (28, 28, 16.0),
    (27, 27, 15.0),
    (26, 26, 14.6),
    (25, 25, 14.4),
    (24, 24, 14.0),
    (23, 23, 13.0),
    (22, 22, 12.6),
    (21, 21, 12.0),
    (20, 20, 11.6),
    (19, 19, 11.0),
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
FEMALE_UNDER_25_HR_PUSHUPS = [
    (32, float('inf'), 20.0),      # > 31
    (30, 31, 19.6),
    (29, 29, 19.2),
    (28, 28, 18.8),
    (27, 27, 18.4),
    (26, 26, 18.0),
    (25, 25, 17.6),
    (24, 24, 17.2),
    (23, 23, 16.8),
    (22, 22, 16.4),
    (21, 21, 16.0),
    (20, 20, 15.6),
    (19, 19, 15.2),
    (18, 18, 14.8),
    (17, 17, 14.4),
    (16, 16, 14.0),
    (15, 15, 13.6),
    (14, 14, 13.2),
    (13, 13, 12.8),
    (12, 12, 12.4),
    (11, 11, 12.0),
    (10, 10, 11.6),
    (9, 9, 11.2),
    (8, 8, 10.8),
    (7, 7, 10.4),
    (6, 6, 10.0),                # 6*
]

# ----------------------
# Strength: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_UNDER_25_SITUPS = [
    (55, float('inf'), 20.0),      # > 54
    (53, 54, 19.7),
    (52, 52, 19.4),
    (51, 51, 19.0),
    (50, 50, 18.8),
    (49, 49, 18.0),
    (48, 48, 17.8),
    (47, 47, 17.6),
    (46, 46, 17.2),
    (45, 45, 17.0),
    (44, 44, 16.0),
    (43, 43, 15.6),
    (42, 42, 15.0),
    (41, 41, 14.0),
    (40, 40, 13.6),
    (39, 39, 13.0),
    (38, 38, 12.0),
    (37, 37, 9.0),
    (36, 36, 6.0),
    (35, 35, 3.0),                # 35*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_UNDER_25_CRUNCH = [
    (48, float('inf'), 20.0),      # > 47
    (46, 47, 19.7),
    (45, 45, 19.4),
    (44, 44, 19.2),
    (43, 43, 18.9),
    (42, 42, 18.6),
    (41, 41, 18.3),
    (40, 40, 18.1),
    (39, 39, 17.8),
    (38, 38, 17.5),
    (37, 37, 17.2),
    (36, 36, 16.9),
    (35, 35, 16.7),
    (34, 34, 16.4),
    (33, 33, 16.1),
    (32, 32, 15.8),
    (31, 31, 15.6),
    (30, 30, 15.3),
    (29, 29, 15.0),
    (28, 28, 14.7),
    (27, 27, 14.4),
    (26, 26, 14.2),
    (25, 25, 13.9),
    (24, 24, 13.6),
    (23, 23, 13.3),
    (22, 22, 13.1),
    (21, 21, 12.8),
    (20, 20, 12.5),
    (19, 19, 12.2),
    (18, 18, 11.9),
    (17, 17, 11.7),
    (16, 16, 11.4),
    (15, 15, 11.1),
    (14, 14, 10.8),
    (13, 13, 10.6),
    (12, 12, 10.3),
    (11, 11, 10.0),                # 11*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
FEMALE_UNDER_25_PLANK = [
    (mmss_to_seconds('3:31'), float('inf'), 20.0),      # > 3:30
    (mmss_to_seconds('3:25'), mmss_to_seconds('3:30'), 19.0),
    (mmss_to_seconds('3:18'), mmss_to_seconds('3:24'), 18.7),
    (mmss_to_seconds('3:12'), mmss_to_seconds('3:17'), 18.5),
    (mmss_to_seconds('3:05'), mmss_to_seconds('3:11'), 18.3),
    (mmss_to_seconds('2:45'), mmss_to_seconds('3:04'), 15.9),
    (mmss_to_seconds('2:25'), mmss_to_seconds('2:44'), 15.2),
    (mmss_to_seconds('2:05'), mmss_to_seconds('2:24'), 14.4),
    (mmss_to_seconds('1:45'), mmss_to_seconds('2:04'), 12.1),
    (mmss_to_seconds('1:25'), mmss_to_seconds('1:44'), 11.3),
    (mmss_to_seconds('1:05'), mmss_to_seconds('1:24'), 10.5),
    (mmss_to_seconds('1:00'), mmss_to_seconds('1:04'), 10.3),
    (mmss_to_seconds('0:55'), mmss_to_seconds('0:59'), 10.0),   # 0:55*
]

# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------
