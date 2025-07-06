# females_40_44.py
# Official USAF PT scoring tables for Females Age 40-44
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
FEMALE_40_44_RUN = [
    (0, mmss_to_seconds('11:22') - 1, 60.0),                 # < 11:22
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:56'), 59.5),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 59.0),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 58.5),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 58.0),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 57.5),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 57.0),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 56.5),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 56.0),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 55.5),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 55.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 54.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 54.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 53.5),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 52.0),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 50.5),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 48.0),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 45.5),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 42.0),
    (mmss_to_seconds('20:34'), mmss_to_seconds('21:28'), 38.5),
    (mmss_to_seconds('21:29'), mmss_to_seconds('22:28'), 35.0), # 22:28*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
FEMALE_40_44_HAMR = [
    (72, float('inf'), 60.0),         # > 71
    (65, 71, 59.5),
    (62, 64, 59.0),
    (59, 61, 58.5),
    (56, 58, 58.0),
    (54, 55, 57.5),
    (51, 53, 57.0),
    (48, 50, 56.5),
    (45, 47, 56.0),
    (42, 44, 55.5),
    (39, 41, 55.0),
    (36, 38, 54.5),
    (33, 35, 54.0),
    (30, 32, 53.5),
    (27, 29, 52.0),
    (24, 26, 50.5),
    (22, 23, 48.0),
    (19, 21, 45.5),
    (16, 18, 42.0),
    (13, 15, 38.5),
    (10, 12, 35.0),                  # 10*-12
]
# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_40_44_PUSHUPS = [
    (39, float('inf'), 20.0),      # > 38
    (37, 38, 19.8),
    (36, 36, 19.6),
    (35, 35, 19.4),
    (34, 34, 19.2),
    (33, 33, 19.0),
    (32, 32, 18.8),
    (31, 31, 18.4),
    (30, 30, 18.2),
    (29, 29, 18.0),
    (28, 28, 17.8),
    (27, 27, 17.6),
    (26, 26, 17.4),
    (25, 25, 17.3),
    (24, 24, 17.2),
    (23, 23, 17.0),
    (22, 22, 16.8),
    (21, 21, 16.6),
    (20, 20, 16.4),
    (19, 19, 16.2),
    (18, 18, 16.0),
    (17, 17, 15.6),
    (16, 16, 15.0),
    (15, 15, 14.0),
    (14, 14, 13.0),
    (13, 13, 12.0),
    (12, 12, 11.0),
    (11, 11, 10.0),
    (10, 10, 7.0),
    (9, 9, 4.0),
    (8, 8, 1.0),                # 8*
]
# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_40_44_HR_PUSHUPS = [
    (29, float('inf'), 20.0),      # > 28
    (27, 28, 19.6),
    (26, 26, 19.2),
    (25, 25, 18.8),
    (24, 24, 18.4),
    (23, 23, 18.0),
    (22, 22, 17.6),
    (21, 21, 17.2),
    (20, 20, 16.8),
    (19, 19, 16.4),
    (18, 18, 16.0),
    (17, 17, 15.6),
    (16, 16, 15.2),
    (15, 15, 14.8),
    (14, 14, 14.4),
    (13, 13, 14.0),
    (12, 12, 13.6),
    (11, 11, 13.2),
    (10, 10, 12.8),
    (9, 9, 12.4),
    (8, 8, 12.0),
    (7, 7, 11.6),
    (6, 6, 11.2),
    (5, 5, 10.8),
    (4, 4, 10.0),                # 4*
]
# ----------------------
# Strength: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_40_44_SITUPS = [
    (42, float('inf'), 20.0),      # > 41
    (40, 41, 19.7),
    (39, 39, 19.4),
    (38, 38, 19.0),
    (37, 37, 18.8),
    (36, 36, 18.4),
    (35, 35, 18.2),
    (34, 34, 18.0),
    (33, 33, 17.6),
    (32, 32, 17.0),
    (31, 31, 16.6),
    (30, 30, 16.4),
    (29, 29, 16.0),
    (28, 28, 15.0),
    (27, 27, 14.0),
    (26, 26, 13.6),
    (25, 25, 12.8),
    (24, 24, 12.0),
    (23, 23, 9.0),
    (22, 22, 6.0),
    (21, 21, 3.0),                # 21*
]
# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_40_44_CRUNCH = [
    (43, float('inf'), 20.0),      # > 42
    (41, 42, 19.7),
    (40, 40, 19.4),
    (39, 39, 19.2),
    (38, 38, 18.9),
    (37, 37, 18.6),
    (36, 36, 18.3),
    (35, 35, 18.1),
    (34, 34, 17.8),
    (33, 33, 17.5),
    (32, 32, 17.2),
    (31, 31, 16.9),
    (30, 30, 16.7),
    (29, 29, 16.4),
    (28, 28, 16.1),
    (27, 27, 15.8),
    (26, 26, 15.6),
    (25, 25, 15.3),
    (24, 24, 15.0),
    (23, 23, 14.7),
    (22, 22, 14.4),
    (21, 21, 14.2),
    (20, 20, 13.9),
    (19, 19, 13.6),
    (18, 18, 13.3),
    (17, 17, 13.1),
    (16, 16, 12.8),
    (15, 15, 12.5),
    (14, 14, 12.2),
    (13, 13, 11.9),
    (12, 12, 11.7),
    (11, 11, 11.4),
    (10, 10, 11.1),
    (9, 9, 10.8),
    (8, 8, 10.6),
    (7, 7, 10.3),
    (6, 6, 10.0),                # 6*
]
# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
FEMALE_40_44_PLANK = [
    (mmss_to_seconds('3:11'), float('inf'), 20.0),      # > 3:10
    (mmss_to_seconds('3:05'), mmss_to_seconds('3:10'), 19.7),
    (mmss_to_seconds('2:59'), mmss_to_seconds('3:04'), 19.3),
    (mmss_to_seconds('2:52'), mmss_to_seconds('2:58'), 18.8),
    (mmss_to_seconds('2:45'), mmss_to_seconds('2:51'), 18.4),
    (mmss_to_seconds('2:25'), mmss_to_seconds('2:44'), 17.1),
    (mmss_to_seconds('2:05'), mmss_to_seconds('2:24'), 15.8),
    (mmss_to_seconds('1:45'), mmss_to_seconds('2:04'), 14.5),
    (mmss_to_seconds('1:25'), mmss_to_seconds('1:44'), 13.2),
    (mmss_to_seconds('1:05'), mmss_to_seconds('1:24'), 11.9),
    (mmss_to_seconds('0:45'), mmss_to_seconds('1:04'), 10.6),
    (mmss_to_seconds('0:40'), mmss_to_seconds('0:44'), 10.3),
    (mmss_to_seconds('0:35'), mmss_to_seconds('0:39'), 10.0), # 0:35*
]
# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------
