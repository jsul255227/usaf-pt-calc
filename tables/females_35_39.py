# females_35_39.py
# Official USAF PT scoring tables for Females Age 35-39
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
FEMALE_35_39_RUN = [
    (0, mmss_to_seconds('11:06') - 1, 60.0),                 # < 11:06
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:38'), 59.5),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 59.0),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 58.5),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 58.0),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 57.5),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 57.0),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 56.5),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 56.0),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 55.5),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 55.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 54.5),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 54.0),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 52.5),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 51.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 49.5),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 47.0),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 44.0),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 41.0),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 38.0),
    (mmss_to_seconds('20:34'), mmss_to_seconds('21:28'), 35.0), # 21:28*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
FEMALE_35_39_HAMR = [
    (75, float('inf'), 60.0),         # > 74
    (68, 74, 59.5),
    (65, 67, 59.0),
    (62, 64, 58.5),
    (59, 61, 58.0),
    (56, 58, 57.5),
    (54, 55, 57.0),
    (51, 53, 56.5),
    (48, 50, 56.0),
    (45, 47, 55.5),
    (42, 44, 55.0),
    (39, 41, 54.5),
    (36, 38, 54.0),
    (33, 35, 52.5),
    (30, 32, 51.0),
    (27, 29, 49.5),
    (24, 26, 47.0),
    (22, 23, 44.0),
    (19, 21, 41.0),
    (16, 18, 38.0),
    (13, 15, 35.0),                  # 13*-15
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_35_39_PUSHUPS = [
    (43, float('inf'), 20.0),      # > 42
    (41, 42, 19.7),
    (40, 40, 19.4),
    (39, 39, 19.0),
    (38, 38, 18.8),
    (37, 37, 18.7),
    (36, 36, 18.6),
    (35, 35, 18.4),
    (34, 34, 18.3),
    (33, 33, 18.1),
    (32, 32, 18.0),
    (31, 31, 17.9),
    (30, 30, 17.8),
    (29, 29, 17.6),
    (28, 28, 17.4),
    (27, 27, 17.3),
    (26, 26, 17.2),
    (25, 25, 17.0),
    (24, 24, 16.6),
    (23, 23, 16.4),
    (22, 22, 16.0),
    (21, 21, 15.8),
    (20, 20, 15.6),
    (19, 19, 15.2),
    (18, 18, 15.0),
    (17, 17, 14.0),
    (16, 16, 13.6),
    (15, 15, 13.0),
    (14, 14, 12.0),
    (13, 13, 10.0),
    (12, 12, 7.0),
    (11, 11, 4.0),
    (10, 10, 1.0),                # 10*
]

# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_35_39_HR_PUSHUPS = [
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
FEMALE_35_39_SITUPS = [
    (44, float('inf'), 20.0),      # > 43
    (42, 43, 19.7),
    (41, 41, 19.4),
    (40, 40, 19.0),
    (39, 39, 18.8),
    (38, 38, 18.0),
    (37, 37, 17.6),
    (36, 36, 17.0),
    (35, 35, 16.6),
    (34, 34, 16.4),
    (33, 33, 16.0),
    (32, 32, 15.6),
    (31, 31, 15.0),
    (30, 30, 14.0),
    (29, 29, 13.6),
    (28, 28, 13.0),
    (27, 27, 12.0),
    (26, 26, 9.0),
    (25, 25, 6.0),
    (24, 24, 3.0),                # 24*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_35_39_CRUNCH = [
    (44, float('inf'), 20.0),      # > 43
    (42, 43, 19.7),
    (41, 41, 19.4),
    (40, 40, 19.2),
    (39, 39, 18.9),
    (38, 38, 18.6),
    (37, 37, 18.3),
    (36, 36, 18.1),
    (35, 35, 17.8),
    (34, 34, 17.5),
    (33, 33, 17.2),
    (32, 32, 16.9),
    (31, 31, 16.7),
    (30, 30, 16.4),
    (29, 29, 16.1),
    (28, 28, 15.8),
    (27, 27, 15.6),
    (26, 26, 15.3),
    (25, 25, 15.0),
    (24, 24, 14.7),
    (23, 23, 14.4),
    (22, 22, 14.2),
    (21, 21, 13.9),
    (20, 20, 13.6),
    (19, 19, 13.3),
    (18, 18, 13.1),
    (17, 17, 12.8),
    (16, 16, 12.5),
    (15, 15, 12.2),
    (14, 14, 11.9),
    (13, 13, 11.7),
    (12, 12, 11.4),
    (11, 11, 11.1),
    (10, 10, 10.8),
    (9, 9, 10.6),
    (8, 8, 10.3),
    (7, 7, 10.0),                # 7*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
FEMALE_35_39_PLANK = [
    (mmss_to_seconds('3:16'), float('inf'), 20.0),      # > 3:15
    (mmss_to_seconds('3:10'), mmss_to_seconds('3:15'), 19.7),
    (mmss_to_seconds('3:04'), mmss_to_seconds('3:09'), 19.3),
    (mmss_to_seconds('2:57'), mmss_to_seconds('3:03'), 18.8),
    (mmss_to_seconds('2:50'), mmss_to_seconds('2:56'), 18.4),
    (mmss_to_seconds('2:30'), mmss_to_seconds('2:49'), 17.1),
    (mmss_to_seconds('2:10'), mmss_to_seconds('2:29'), 15.8),
    (mmss_to_seconds('1:50'), mmss_to_seconds('2:09'), 14.5),
    (mmss_to_seconds('1:30'), mmss_to_seconds('1:49'), 13.2),
    (mmss_to_seconds('1:10'), mmss_to_seconds('1:29'), 11.9),
    (mmss_to_seconds('0:50'), mmss_to_seconds('1:09'), 10.6),
    (mmss_to_seconds('0:45'), mmss_to_seconds('0:49'), 10.3),
    (0, mmss_to_seconds('0:44'), 10.0),                  # <= 0:44
]
# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------
